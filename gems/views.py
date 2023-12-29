from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import (
    HttpResponseRedirect, HttpResponse, HttpResponseForbidden)
from django.views import generic, View
from .models import Post, Webinar, Timestamp, Booking, Comment
from .forms import CommentForm
from django.contrib import messages
from django.db import IntegrityError


def about(request):
    """About Page"""
    return render(request, 'about.html')


def webinar(request):
    """Webinar list page"""
    return render(request, 'webinars.html')


def contact(request):
    """Contact us page"""
    return render(request, 'contact_us.html')


class AdminQuickDeleteComment(View):

    """ Used the following link for help with admin deleting comments from the
    frontend comment box https://www.youtube.com/watch?v=CIR2QhX5mqA"""

    def is_superuser(self):
        return self.request.user.is_superuser

    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect('location_detail', slug=comment.post.slug)

    def post(self, request, comment_id):
        if not self.is_superuser():
            return HttpResponseForbidden(
                "You are not authorised to make this request")

        comment = get_object_or_404(Comment, id=comment_id)
        post_slug = comment.post.slug
        comment.delete()
        return redirect('location_detail', slug=post_slug)


""" Blog post list"""


class PostList(generic.ListView):

    """Create post list on index page with 6 posts per page.
    Ordering in newest first"""

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


""" Webinar post list """


class WebinarList(generic.ListView):

    """Create webinar list within the webinars page with 6 posts per page.
    Ordering in newest first"""

    model = Webinar
    queryset = Webinar.objects.filter(status=1).order_by('-created_on')
    template_name = 'webinars.html'
    paginate_by = 6


""" Webinar detail page """


class WebinarDetail(View):

    """ To display webinar with timestamps available for the user to book """

    def get(self, request, slug, *args, **kwargs):
        webinar = get_object_or_404(Webinar, slug=slug)
        timestamps = Timestamp.objects.filter(
            webinar=webinar).order_by('date_and_time')

        return render(request, 'webinar_detail.html', {
            'webinar': webinar,
            'timestamps': timestamps
        }
        )


""" Make a booking """


class Book(View):

    """ For making a booking and selecting the amount of viewers attending.
    User must be signed in, if not the user is redirected to the sign in page.
    Total views has to be a minimum of 1. All ready booked users will be
    redirected to a page informing them the booking is already booked and
    waiting approval"""

    def get(self, request, timestamp_id):
        timestamp = get_object_or_404(Timestamp, id=timestamp_id)
        context = {
            'timestamp': timestamp
        }

        return render(request, 'my_bookings.html', context)

    def post(self, request, timestamp_id):
        timestamp = get_object_or_404(Timestamp, id=timestamp_id)

        try:
            # Check users authentication, if yes create a new booking
            if request.user.is_authenticated:
                total_viewers = int(request.POST.get('total_viewers', 1))
                booking = Booking.objects.create(
                    user=request.user,
                    webinar=timestamp,
                    approved=False,
                    number_of_viewers=total_viewers)

                return render(request, 'my_bookings.html', {
                    'pending_approval': True
                })
            else:
                # if not authenticated,
                # # send user to login page with error message
                messages.error(
                    request, 'You need to be signed in to book a webinar.')
                return redirect('account_login')
        except IntegrityError:
            # Handle IntegrityError (prevent double booking attempt)
            return render(request, 'my_bookings.html', {
                'already_booked': True,
            })


""" Update webinar booking """


class UpdateBooking(View):

    """ If the booking has been approved, update booking is available,
    once updated the users booking page will refresh for the new amount
    of viewers """

    def post(self, request, booking_id):
        booking_update = get_object_or_404(
            Booking, id=booking_id, user=request.user, approved=True)
        total_viewers = int(request.POST.get('total_viewers', 1))
        booking_update.number_of_viewers = total_viewers
        booking_update.save()
        return redirect('my-bookings')


""" Booking page """


class MyBooking(View):

    """ For viewing bookings once they have been approved by admin. Delete the
    booking and the users booking will update to a updated list of bookings.
    Used 'https://stackoverflow.com/questions/47899265/
    order-by-time-of-a-datetime-field-in-django'
    to help with ordering the bookings by date and time"""

    def get(self, request):
        booking_approved = Booking.objects.filter(
            user=request.user, approved=True).order_by(
                'webinar__date_and_time')
        if booking_approved:
            return render(request, 'my_bookings.html', {
                'booking_approved': booking_approved,
                'approved': True,
            })
        else:
            return render(request, 'my_bookings.html', {
                'approved': False,
            })

    """ For users to delete a booking """

    def post(self, request, booking_id):
        booking_delete = get_object_or_404(
            Booking, id=booking_id, user=request.user, approved=True)
        booking_delete.delete()
        return redirect('my-bookings')


""" location detail """


class PostDetail(View):

    """ For displaying the loaction detail related to the post.
    Likes being displayed linked with the user id. Comments being displayed
    with most recent first. Comments being checked if valid and informing
    the user of a successful comment or unsuccessful comment """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'location_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    """ Posting comments """

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(
                request, 'Comment successfully submitted'
                ' and awaiting approval.')
        else:
            comment_form = CommentForm()
            messages.error(
                request, 'Unable to submit your'
                'comment at this time, please try again.')

        return render(
            request,
            'location_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


""" Liking posts """


class PostLike(View):

    """ For liking a post and also removing the like within the
    blog post post """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('location_detail', args=[slug]))


def error_404(request, exception):

    """"
    Handles HTTP 404 errors
    """

    return render(request, '404.html')


def error_500(request, exception):

    """"
    Handles HTTP 500 errors
    """

    return render(request, '500.html')

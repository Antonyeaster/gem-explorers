from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
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

    """ https://www.youtube.com/watch?v=CIR2QhX5mqA 
    for help with deleting comment on frontend """

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

    """Create post list on index page with 6 posts per page"""

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


""" Webinar post list """


class WebinarList(generic.ListView):

    """Create webinar list within the webinars page with 4 posts per page"""

    model = Webinar
    queryset = Webinar.objects.filter(status=1).order_by('-created_on')
    template_name = 'webinars.html'
    paginate_by = 6


""" Webinar detail page """


class WebinarDetail(View):

    """ To display webinar detail for user to read then book """

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

    """ For making a booking and selecting the amount of viewers attending
    must be signed in"""

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
                # send user to login page with error message
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

    """ To update webinar viewers amount """

    def post(self, request, booking_id):
        booking_update = get_object_or_404(
            Booking, id=booking_id, user=request.user, approved=True)
        total_viewers = int(request.POST.get('total_viewers', 1))
        booking_update.number_of_viewers = total_viewers
        booking_update.save()
        return redirect('my-bookings')


""" Booking page """


class MyBooking(View):

    """ For viewing bookings once they have been approved by admin """

    def get(self, request):
        booking_approved = Booking.objects.filter(
            user=request.user, approved=True)
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


""" location detail page including likes and comments """


class PostDetail(View):

    """ For displaying the loaction detail related to the post """

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

    """ To create a comment and display users details"""

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

    """ For liking a post and also removing the like """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('location_detail', args=[slug]))


""" https://medium.com/@yildirimabdrhm/python-django-handling-custom-error-page-807087352bea """


def error_404(request, exception):
    """ 404 Page Not Found """
    return render(request, 'errors/404.html', status=404)


def error_500(request):
    """ 500 Internal Server Error """
    return render(request, 'errors/500.html', status=500)


def error_403(request, exception):
    """ 403 Forbidden """
    return render(request, 'errors/403.html', status=403)


def error_400(request, exception):
    """ 400 Bad Request """
    return render(request, 'errors/400.html', status=400)

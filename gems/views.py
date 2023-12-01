from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic, View
from .models import Post, Webinar, Timestamp, Booking
from .forms import CommentForm
from django.contrib import messages
from django.db import IntegrityError


"""About Page """


def about(request):
    return render(request, 'about.html')


def webinar(request):
    return render(request, 'webinars.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


class WebinarList(generic.ListView):
    model = Webinar
    queryset = Webinar.objects.filter(status=1).order_by('-created_on')
    template_name = 'webinars.html'
    paginate_by = 4


class WebinarDetail(View):

    def get(self, request, slug, *args, **kwargs):
        webinar = get_object_or_404(Webinar, slug=slug)
        timestamps = Timestamp.objects.filter(
            webinar=webinar).order_by('date_and_time')

        return render(request, 'webinar_detail.html', {
            'webinar': webinar,
            'timestamps': timestamps
        }
        )


class Book(View):

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
                # if not authenticated, send user to login page
                return redirect('account_login')
        except IntegrityError:
            # Handle IntegrityError (prevent double booking attempt)
            return render(request, 'my_bookings.html', {
                'already_booked': True,
            })


class UpdateBooking(View):
    def post(self, request, booking_id):
        booking_update = get_object_or_404(
            Booking, id=booking_id, user=request.user, approved=True)
        total_viewers = int(request.POST.get('total_viewers', 1))
        booking_update.number_of_viewers = total_viewers
        booking_update.save()
        return redirect('my-bookings')

        
class MyBooking(View):

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

    def post(self, request, booking_id):
        booking_delete = get_object_or_404(
            Booking, id=booking_id, user=request.user, approved=True)
        booking_delete.delete()
        return redirect('my-bookings')


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
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

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
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
                'and awaiting approval.')
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


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('location_detail', args=[slug]))

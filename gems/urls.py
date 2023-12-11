from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('webinar/', views.WebinarList.as_view(), name='webinar'),
    path('webinar/<slug:slug>/',
         views.WebinarDetail.as_view(), name='webinar_detail'),
    path('book/<int:timestamp_id>/', views.Book.as_view(), name='book'),
    path('my-bookings/', views.MyBooking.as_view(), name='my-bookings'),
    path('my-bookings/<int:booking_id>/',
         views.MyBooking.as_view(), name='booking_delete'),
    path('update-booking/<int:booking_id>/',
         views.UpdateBooking.as_view(), name='update-booking'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='location_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('delete_comment/<int:comment_id>/',
         views.AdminQuickDeleteComment.as_view(), name='delete_comment'),
]

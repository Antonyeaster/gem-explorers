from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('webinar/', views.WebinarList.as_view(), name='webinar'),
    path('webinar/<slug:slug>/',
         views.WebinarDetail.as_view(), name='webinar_detail'),
    path('book/<str:timestamp_id>/', views.Book.as_view(), name='book'),
    path('my-bookings/', views.MyBooking.as_view(), name='my-bookings'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='location_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

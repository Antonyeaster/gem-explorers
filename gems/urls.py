from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('webinar/', views.WebinarList.as_view(), name='webinar'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='location_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

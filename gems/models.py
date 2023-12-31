from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

"""Blog posts"""


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):

    """ Post model - all fields required for creating a blog post using
    cloudinary for the featured image and a ordering of most recent
    posts displayed first """

    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    location = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


""" Post Comments"""


class Comment(models.Model):

    """ For commenting on the posts in the blog section,
    approval is required before the post is published and comments are
    ordered in newest posts first """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f'Comment {self.body} by {self.name}'


"""Webinar"""


STATUS = ((0, "Draft"), (1, "Published"))


class Webinar(models.Model):

    """ Webinar model - all fields required for creating a webinar post using
    cloudinary for the featured image and a ordering of most recent
    webinars displayed first """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    speaker = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


"""Webinar booking """


class Timestamp(models.Model):

    """Timestamp model - linked with Webinar model for correct webinar to
    timestamp. Unique constraint to ensure there are no double bookings"""

    webinar = models.ForeignKey(
        Webinar, on_delete=models.CASCADE, related_name='approved_webinar')
    date_and_time = models.DateTimeField()

    class Meta:
        ordering = ['date_and_time']
        constraints = [
            models.UniqueConstraint(
                fields=['webinar', 'date_and_time'],
                name='unique_webinar_date_and_time_constraint'
            ),
        ]

    def __str__(self):
        return f'{self.webinar.title} scheduled for {self.date_and_time}'


"""Booked webinar """


class Booking(models.Model):

    """ Booking model - Linked with the user that created the booking.
    Linked with the timestamp the user selected. Unique constraint to
    ensure only one booking per user and webinar"""
 
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_bookings')
    webinar = models.ForeignKey(
        Timestamp, on_delete=models.CASCADE, related_name='webinar_bookings')
    number_of_viewers = models.PositiveIntegerField(default=1)
    approved = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['webinar', 'user'],
                name='unique_webinar_user_constraint'
            ),
        ]

    def __str__(self):
        return (
            f'{self.user.username} booked '
            f'{self.webinar} '
            f'on {self.webinar.date_and_time}'
        )

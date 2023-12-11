from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


"""Blog Post"""


STATUS = ((0, "Draft"), (1, "Published"))

"""Post model"""


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
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


"""Webinar booking time (No double bookings)"""


class Timestamp(models.Model):
    webinar = models.ForeignKey(
        Webinar, on_delete=models.CASCADE, related_name='approved_webinar')
    date_and_time = models.DateTimeField()
    booked = models.BooleanField(default=False)

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


"""Booked webinar (No double bookings)"""


class Booking(models.Model):
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

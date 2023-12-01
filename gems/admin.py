from django.contrib import admin
from .models import Post, Comment, Webinar, Booking, Timestamp
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'webinar', 'approved', 'number_of_viewers')
    list_filter = ('webinar', 'approved')
    search_fields = ('user__username', 'user__email', 'webinar__title')
    actions = ['approve_bookings']

    def user_name(self, obj):
        return obj.user.username

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Timestamp)
class TimestampAdmin(SummernoteModelAdmin):
    list_display = ('webinar', 'date_and_time')
    search_fields = ('title', 'speaker', 'content')
    summernote_fields = ('content')


@admin.register(Webinar)
class WebinarAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'updated_on', 'speaker')
    summernote_fields = ('content',)
    search_fields = ['title', 'content', 'speaker']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on',)

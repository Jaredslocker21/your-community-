from django.contrib import admin
from .models import CommunityPost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CommunityPost)
class CommunityPostAdmin(SummernoteModelAdmin):
    """
    This class displays a summernote model and  a nice list filter
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('blurb')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class displays admin model shown in the admin panel 
    for the admin
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """ Comments to be approved """
        queryset.update(approved=True)
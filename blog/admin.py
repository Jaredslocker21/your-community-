from django.contrib import admin
from .models import CommunityPost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CommunityPost)
class CommunityPostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('blurb')


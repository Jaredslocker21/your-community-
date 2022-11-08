from django.shortcuts import render
from django.views import generic
from .models import CommunityPost

# Create your views here.


class PostList(generic.ListView):
    model = CommunityPost
    queryset = CommunityPost.objects.filter().order_by('-created_on')
    template_name = 'index.html'
    paginated_by = 6
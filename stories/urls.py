from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from .views import CreateStoryView, StoryDetailView, ChapterDetailView


urlpatterns = patterns('',
    url(r'^start-story/$', login_required(CreateStoryView.as_view()), name='create_story'),
    url(r'^story/(?P<slug>[-_\w]+)/$', StoryDetailView.as_view(), name='story_detail'),
    url(r'^chapter/(?P<pk>\d+)/$', ChapterDetailView.as_view(), name='chapter_detail'),
)

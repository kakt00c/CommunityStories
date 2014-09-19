from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404

from .models import Story, Chapter
from .forms import CreateStoryForm, AddChapterForm


class CreateStoryView(FormView):
    new_story = None
    template_name = 'stories/create_story.html'
    form_class = CreateStoryForm
    
    def form_valid(self, form):
        data = form.cleaned_data
        self.new_story = Story(title=data['title'])
        self.new_story.save()
        chapter = Chapter(story=self.new_story,
                          headline=data['headline'], body=data['body'])
        chapter.save()
        return super(CreateStoryView, self).form_valid(form)
    
    def get_success_url(self):
        kwargs = {'slug': self.new_story.slug}
        return reverse('story_detail', kwargs=kwargs)


class StoryDetailView(DetailView):
    model = Story
    
    def get_context_data(self, *args, **kwarks):
        context = super(StoryDetailView, self).get_context_data(*args, **kwarks)
        first_chapter = Chapter.objects.get(story=self.object,
                                            parent__isnull=True)
        context['first_chapter_pk'] = first_chapter.pk
        return context


class ChapterDetailView(FormView):
    current_chapter = None
    new_chapter = None
    template_name = 'stories/chapter_detail.html'
    form_class = AddChapterForm

    def get_context_data(self, *args, **kwargs):
        context = super(ChapterDetailView, self).get_context_data(*args, **kwargs)
        self.current_chapter = get_object_or_404(Chapter, pk=self.kwargs['pk'])
        children = Chapter.objects.filter(parent=self.current_chapter)
        children = children.only('headline')
        context['chapter'] = self.current_chapter
        context['chapter_children'] = children
        return context
    
    def get_form_kwargs(self):
        self.current_chapter = get_object_or_404(Chapter, pk=self.kwargs['pk'])
        kwargs = super(ChapterDetailView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_initial(self):
        return {'parent': self.current_chapter.pk}
    
    def form_valid(self, form):
        self.new_chapter = form.save()
        return super(ChapterDetailView, self).form_valid(form)
    
    def get_success_url(self):
        kwargs = {'pk': self.new_chapter.pk}
        return reverse('chapter_detail', kwargs=kwargs)

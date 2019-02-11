from django.views.generic import TemplateView
from django.shortcuts import render

from .models import Job
from blog.models import Blog
# Create your views here.

class Allview(TemplateView):

    template_name = 'jobs/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(Allview, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['jobs'] = Job.objects.all().order_by('-id')[:3]
        context['blogs'] = Blog.objects.all()
        return context


def about(request):
    jobs = Job.objects
    return render(request, 'jobs/aboutme.html', {'jobs':jobs})








from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
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

# Create your views here.
def alljobs(request):
    jobs = Job.objects
    return render(request, 'jobs/allprojects.html', {'jobs':jobs})

def jobdetail(request, job_id):
    detailjob = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/projectdetail.html', {'job':detailjob})





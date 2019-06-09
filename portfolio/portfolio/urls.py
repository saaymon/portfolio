from django.views.generic.list import ListView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jobs.views import Allview
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Allview.as_view(), name='home'),
    path('about/', jobs.views.about, name='about'),
    path('blog/', include('blog.urls')),
    path('job/', include('jobs.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

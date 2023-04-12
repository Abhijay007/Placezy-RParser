from scrapper.views import resumeparser
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('resume-parser/', resumeparser.as_view(), name='resume-parser'),

] 
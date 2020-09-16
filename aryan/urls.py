from .views import *
from django.conf.urls import url
from django.urls import include,path

app_name = 'cv'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    path('teams', TeamView.as_view(), name='teams'),
    path('about',AboutView.as_view(),name='about'),
    path('rewards',RewardsView.as_view(),name='rewards'),
    path('blogs',BlogsView.as_view(),name='blogs'),
    path('blog/',BlogsingleView.as_view(),name='blog'),
    path('contact',ContactView.as_view(),name='contact'),
]

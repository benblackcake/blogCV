
from django.urls import path, include
from django.views.generic import TemplateView
from blogPost.views import *

app_name='blogPost'
urlpatterns=[
    path('',PostAllView.as_view(),name='blogpost'),
    path('/detial/<id>',PostDetialView.as_view(),name='detial'),
    path('/entry',TemplateView.as_view(template_name='entry.html'),name='entry'),
]
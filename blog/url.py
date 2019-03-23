from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from blog.views import *


app_name='blogCV'
router = DefaultRouter()
router.register('post',PostSerializerView)
router.register('user',ValidateStaffUser)
router.register('comment',PostCommentSerializerView)

urlpatterns=[
    path('api/',include(router.urls),name='api'),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('logout',ValidateStaffUserLogout.as_view(),name='logout'),

]
from django.shortcuts import render, redirect
# Create your views here.
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import *
from blog.serializers import *

class PostAllView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    # permission_classes = [permissions.AllowAny]
    template_name = 'blogpost.html'

    def get(self,request,format=None):
        queryset=BlogPost.objects.all()
        print(queryset)
        return Response({'datas':queryset})

    # def post(self,request, *args, **kwargs):
    #     serializer=PostSerializers(data=request.data,
    #                                   context={'request':request})
    #     print(serializer)
    #     if serializer.is_valid():
    #         serializer.save(user_id=self.request.user)
    #     return redirect('blogPost:blogpost')

class PostDetialView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='detial.html'
    comment=''
    def get(self,request,id):

        queryset=BlogPost.objects.get(id=id)
        try:
            self.comment=BlogComment.objects.filter(post=id)
            # print(self.comment.context)
        except BlogComment.DoesNotExist:
            pass
        # print(queryset)
        return Response({'datas':queryset,
                         'comments':self.comment})


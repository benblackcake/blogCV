from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import *
from blog.models import *
from rest_framework import viewsets
from datetime import time, datetime
# Create your views here.



class PostSerializerView(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    queryset = BlogPost.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=PostSerializers(data=request.data,
                                      context={'request':request})
        now=datetime.now().date()
        print(now)
        print(serializer)
        if serializer.is_valid():
            serializer.save(user_id=self.request.user,
                            post_date=now)
        return redirect('blogPost:blogpost')

class PostCommentSerializerView(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    queryset = BlogComment.objects.all()

    def create(self, request, *args, **kwargs):
        now = datetime.now().date()
        serializer=CommentSerializers(data=request.data,
                                      context={'request':request})
        if serializer.is_valid():
            serializer.save(comment_date=now)
        return HttpResponse()

class CatlogSerializerView(viewsets.ModelViewSet):
    serializer_class = CatlogSerializers
    queryset = BlogCatlog.objects.all()



class ValidateStaffUser(viewsets.ModelViewSet):
    serializer_class = StaffUserAuth
    queryset = User.objects.all()

    # def list(self, request, *args, **kwargs):
    #     serializer=StaffUserAuth
    #     return Response({'serializer': serializer.data})
    # # def get(self,request):
    # #     serializer=StaffUserAuth
    # #     return Response({'serializer': serializer})

    def create(self, request, *args, **kwargs):
        try:
            serializer=StaffUserAuth(data=request.data)
            if serializer.is_valid():
                user=serializer.validate(request.data)
                # uer=AuthtokenToken.objects.filter(user_id=user).values('key')
                if user.is_staff:
                    print(user)
                    login(request,user)
                    return HttpResponse({'success'})
        except AssertionError:
            return HttpResponse({'unsuccess'})
        return HttpResponse({'unsuccess'})

class ValidateStaffUserLogout(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'logout.html'

    def get(self,request,format=None):
        logout(request)
        return redirect("blogCV:index")
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_permission_codename

from blog.models import *


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=('post_title','post_context','post_context')


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model=BlogComment
        fields=('username','context','post')
class CatlogSerializers(serializers.ModelSerializer):
    class Meta:
        model=BlogCatlog
        fields=('__all__')

class StaffUserAuth(serializers.ModelSerializer):
    username=serializers.CharField(
        max_length=30,
        required=True
    )
    password=serializers.CharField(
        max_length=30,
        required=True,
        style={
            'input_type': 'password', 'placeholder': 'Password'
        }
    )
    def validate(self, attrs):
        credentials={
            'username':attrs.get('username'),
            'password':attrs.get('password')
        }
        if all(credentials.values()):
            user=authenticate(**credentials)

            # user
            # token=Token.objects.get(user=user)
            return(user)
    class Meta:
        model=User
        fields=('username','password')
from blog.api.serializers import UserSerializer,Postserializer,Commentserializer,Profileserializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from blog.models import Post,Comment,Profile
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UsertestViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer  
    lookup_field='username'
class PostViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Post.objects.all()
    serializer_class=Postserializer
    lookup_field='author'
class PostbyidViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Post.objects.all()
    serializer_class=Postserializer
    lookup_field='id'
class CommentViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Comment.objects.all()
    serializer_class=Commentserializer
class ProfileViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Profile.objects.all()
    serializer_class=Profileserializer
    lookup_field='user'

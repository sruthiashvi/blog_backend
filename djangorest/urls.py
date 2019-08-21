from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from blog.api.viewsets import UsertestViewSet,UserViewSet,PostViewSet,CommentViewSet,PostbyidViewSet,ProfileViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
 #automaticaly include crud methods
router.register('users',UserViewSet)
router.register('userbynum',UsertestViewSet)
router.register('posts',PostViewSet)
router.register('comments',CommentViewSet)
router.register('postsbyid',PostbyidViewSet)
router.register('profile',ProfileViewSet)

#router.register(r'login',viewsets.LoginViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^",include("blog.urls")),
    path('api/',include(router.urls)), #localhost:8000/api/plans/1/delete 
   path('auth/',obtain_auth_token)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from blog.models import Post,Comment,Profile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','email','first_name','last_name') 
        extra_kwargs={'password':{'write_only':True,'required':True}} 
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user 
class Postserializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id','author','subject','content','pdate','ptime')
class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('id','pid','postedby','comment','cdate','ctime')
class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('id','user','image')        



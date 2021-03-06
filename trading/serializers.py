from rest_framework import serializers
from .models import *
from users.models import *
from chat.models import Message
from django.contrib.auth.models import User


class FriendRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return User.objects.get(username=data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Profile
        fields = ("id",'user','user_name','friends',"image")
    


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id','author','author_name',"author_image",'img','video','content','date_posted']

# class FriendNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username']

class FriendSerializer(serializers.ModelSerializer):
    friend_name = FriendRelatedField(
            queryset=User.objects.all(),
            many=True
        )
    # friend_name = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    user_name = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Friend_List
        fields = ['id','user','user_name','friend_name']
     
    

class ChatSerializer(serializers.ModelSerializer):
    # author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Message
        fields = ['id','sender','receiver','message','timestamp','is_read']


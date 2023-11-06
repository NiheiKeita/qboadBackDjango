from rest_framework import serializers
import logging
from django.utils.crypto import get_random_string
from apiapp.models import Question, Choice, User, PasswordReset,ResultSolve,Comment,HashTag,QuestionLike,Follow,MyList,MyListQuestion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
    def create(self, validated_data):
        validated_data['unique_user_id'] = self.createUniqueId()
        return User.objects.create(**validated_data)

    def createUniqueId(self):
        result = get_random_string(10).lower()
        queryset = User.objects.all()
        if (queryset.filter(unique_user_id = result).count() > 0):
            self.createUniqueId()
        else:
            return result

        
class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordReset
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ResultSolveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultSolve
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
class QuestionLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionLike
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
class MyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyList
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class MyListQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyListQuestion
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
from rest_framework import serializers
from apiapp.models import Question, Choice, User, PasswordReset,ResultSolve,Comment,HashTag,QuestionLike,Follow,MyList,MyListQuestion

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
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
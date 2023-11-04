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

class ResultSolve(serializers.ModelSerializer):
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
        
class Comment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
class HashTag(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
class QuestionLike(serializers.ModelSerializer):
    class Meta:
        model = QuestionLike
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
class Follow(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
class MyList(serializers.ModelSerializer):
    class Meta:
        model = MyList
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class MyListQuestion(serializers.ModelSerializer):
    class Meta:
        model = MyListQuestion
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
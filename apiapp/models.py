from django.db import models
from django_boost.models.mixins import LogicalDeletionMixin

class User(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200,blank=True, null=True)
    unique_user_id = models.CharField(max_length=200,blank=True, null=True)

class PasswordReset(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=240)
    taken = models.CharField(max_length=200)

class Question(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_content = models.TextField(blank=True, null=True)

class Choice(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_content = models.CharField(max_length=200,blank=True, null=True)
    is_correct = models.IntegerField(default=0)

class ResultSolve(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiced_content = models.CharField(max_length=200,blank=True, null=True)
    is_correct = models.IntegerField(default=0)

class Profile(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_content = models.TextField(blank=True, null=True)
    
class Comment(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.TextField(blank=True, null=True)
    
class HashTag(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hash_tag_content = models.CharField(max_length=200,blank=True, null=True)
    
class QuestionLike(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
class Follow(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow_user_id = models.IntegerField()
    
class MyList(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_list_name = models.CharField(max_length=200,blank=True, null=True)
    
class MyListQuestion(LogicalDeletionMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    myList = models.ForeignKey(MyList, on_delete=models.CASCADE)
    sort = models.IntegerField(default=0)
    
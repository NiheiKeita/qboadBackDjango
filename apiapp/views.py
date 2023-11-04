from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question, Choice, User, PasswordReset,ResultSolve,Comment,HashTag,QuestionLike,Follow,MyList,MyListQuestion
from .serializers import UserSerializer,QuestionSerializer,ChoiceSerializer,PasswordResetSerializer,ResultSolveSerializer,CommentSerializer,HashTagSerializer,QuestionLikeSerializer,FollowSerializer,MyListSerializer,MyListQuestionSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        products = User.objects.all()
        serializer = UserSerializer(products, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    
class PasswordResetViewSet(viewsets.ModelViewSet):
    queryset = PasswordReset.objects.all()
    serializer_class = PasswordResetSerializer
    
class ResultSolveViewSet(viewsets.ModelViewSet):
    queryset = ResultSolve.objects.all()
    serializer_class = ResultSolveSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class HashTagViewSet(viewsets.ModelViewSet):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer

class QuestionLikeViewSet(viewsets.ModelViewSet):
    queryset = QuestionLike.objects.all()
    serializer_class = QuestionLikeSerializer

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

class MyListViewSet(viewsets.ModelViewSet):
    queryset = MyList.objects.all()
    serializer_class = MyListSerializer
    
class MyListQuestionViewSet(viewsets.ModelViewSet):
    queryset = MyListQuestion.objects.all()
    serializer_class = MyListQuestionSerializer
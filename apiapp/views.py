from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated

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
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # @api_view(['GET'])
    # def users(self, request, pk=None):
    #     return Response({'status': 'password set'})
    
class QuestionViewSet(viewsets.ModelViewSet):
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class ChoiceViewSet(viewsets.ModelViewSet):
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    
class PasswordResetViewSet(viewsets.ModelViewSet):
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = PasswordReset.objects.all()
    serializer_class = PasswordResetSerializer
    
class ResultSolveViewSet(viewsets.ModelViewSet):
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = ResultSolve.objects.all()
    serializer_class = ResultSolveSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class HashTagViewSet(viewsets.ModelViewSet):
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer

class QuestionLikeViewSet(viewsets.ModelViewSet):
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = QuestionLike.objects.all()
    serializer_class = QuestionLikeSerializer

class FollowViewSet(viewsets.ModelViewSet):
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

class MyListViewSet(viewsets.ModelViewSet):
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = MyList.objects.all()
    serializer_class = MyListSerializer
    
class MyListQuestionViewSet(viewsets.ModelViewSet):
    # permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = MyListQuestion.objects.all()
    serializer_class = MyListQuestionSerializer
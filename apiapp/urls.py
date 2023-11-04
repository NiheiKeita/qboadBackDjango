from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from apiapp import apis
from .views import users,UserViewSet,QuestionViewSet,ChoiceViewSet,PasswordResetViewSet,ResultSolveViewSet,CommentViewSet,HashTagViewSet,QuestionLikeViewSet,FollowViewSet,MyListViewSet,MyListQuestionViewSet

router = DefaultRouter()
# router.register('users', users)
router.register('users', UserViewSet)
router.register('questions', QuestionViewSet)
router.register('choices', ChoiceViewSet)
router.register('password_resets', PasswordResetViewSet)
router.register('result_solves', ResultSolveViewSet)
router.register('comments', CommentViewSet)
router.register('hash_tags', HashTagViewSet)
router.register('question_likes', QuestionLikeViewSet)
router.register('follows', FollowViewSet)
router.register('my_lists', MyListViewSet)
router.register('my_list_question', MyListQuestionViewSet)

urlpatterns = [
    # path("", views.index, name="index"),
    path('', include(router.urls)),
    
]
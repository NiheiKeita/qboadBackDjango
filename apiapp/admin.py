from django.contrib import admin

# Register your models here.

from apiapp.models import Question, Choice, User, PasswordReset,ResultSolve,Comment,HashTag,QuestionLike,Follow,MyList,MyListQuestion

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)
admin.site.register(PasswordReset)
admin.site.register(ResultSolve)
admin.site.register(Comment)
admin.site.register(HashTag)
admin.site.register(QuestionLike)
admin.site.register(Follow)
admin.site.register(MyList)
admin.site.register(MyListQuestion)
from django.urls import path
from .views import *

app_name = "qnapage"

urlpatterns = [
    path('qnalistrecent/', qnalistrecent, name="qnalistrecent"),
    path('qnalistpop/', qnalistpop, name="qnalistpop"),
    path('create/', create, name="create"),
    path('new/', new, name="new"),
    path('qnadetail/<int:id>/', qnadetail, name="qnadetail"),
]
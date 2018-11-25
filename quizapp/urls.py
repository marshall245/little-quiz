from django.urls import path

from . import views


app_name = 'quizapp'

urlpatterns = [
    # ex: /quizapp/
    path('', views.index, name='index'),
    # ex: /quizapp/5/
    path('<int:quiz_id>/', views.quiz, name='quiz'),
    # ex: /quizapp/4/result/
    path('<int:quiz_id>/quiz_solution/', views.quiz_solution, name='quiz_solution'),
]
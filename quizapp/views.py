from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quiz, Choice


def index(request):
    # show quizes
    latest_quiz_list = Quiz.objects.order_by('-pub_date')[:10]
    return render(request, 'quizapp/index.html', {'latest_quiz_list': latest_quiz_list})


def quiz(request, quiz_id):
    # show quiz
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quizapp/quiz.html', {'quiz': quiz})


def quiz_solution(request, quiz_id):
    # show the results of a quiz submission
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    correct_ct = wrong_ct = 0
    for question in quiz.question_set.all():
        q_choice_val = request.POST[question.question_name][0]
        choice_truth = get_object_or_404(Choice, pk=q_choice_val)
        if choice_truth.is_correct:
            correct_ct += 1
        else:
            wrong_ct += 1

    response_body = '# Total : %s<br># Correct : %d<br># Wrong : %d'
    return HttpResponse(response_body % (correct_ct + wrong_ct, correct_ct, wrong_ct))

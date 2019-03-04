# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from DjangoSample import settings
from .models import Question, Choice

"""
视图函数文件
"""


def index(request):
    print settings.STATIC_ROOT
    latest_question_list = Question.objects.filter(pub_date__lte=datetime.now()).order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'ch01/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.filter(pub_date__lte=datetime.now()).get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("查看的问题不存在！")
    return render(request, 'ch01/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'ch01/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ch01/detail.html', {
            'question': question,
            'error_message': "你没有选择一个选项。",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('ch01:results', args=(question.id,)))

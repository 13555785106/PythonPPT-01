# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse

from .models import Question

"""
单元测试文件
"""


def question_is_recently(hours=48):
    time = datetime.now() + timedelta(hours=hours)
    question = Question(pub_date=time)
    return question.was_published_recently()


# python manage.py test ch01
class QuestionModelTests(TestCase):

    # 所有以test开头的函数会被运行
    def test_was_published_recently_01(self):
        self.assertIs(question_is_recently(), False)

    def test_was_published_recently_02(self):
        self.assertIs(question_is_recently(hours=-48), True)

    def test_was_published_recently_03(self):
        self.assertIs(question_is_recently(hours=-76), False)


def create_question(question_text, days):
    time = datetime.now() + timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse('ch01:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "没有投票可用")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question(question_text="过去的问题", days=-30)
        response = self.client.get(reverse('ch01:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: 过去的问题>'.encode('UTF-8')]
        )

    def test_future_question(self):
        create_question(question_text="将来的问题", days=30)
        response = self.client.get(reverse('ch01:index'))
        self.assertContains(response, "没有投票可用")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        create_question(question_text="过去的问题", days=-30)
        create_question(question_text="将来的问题", days=30)
        response = self.client.get(reverse('ch01:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: 过去的问题>'.encode('UTF-8')]
        )

    def test_two_past_questions(self):
        create_question(question_text="过去的问题1", days=-30)
        create_question(question_text="过去的问题2", days=-5)
        response = self.client.get(reverse('ch01:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: 过去的问题2>'.encode('UTF-8'), '<Question: 过去的问题1>'.encode('UTF-8')]
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='将来的问题', days=5)
        url = reverse('ch01:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text='过去的问题', days=-5)
        url = reverse('ch01:detail', args=(past_question.id,))
        response = self.client.get(url)
        print response
        self.assertContains(response, past_question.question_text)

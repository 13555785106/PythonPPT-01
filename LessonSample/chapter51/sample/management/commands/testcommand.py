#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = '命令测试'

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        for poll_id in options['poll_id']:
            print poll_id
        if options['delete']:
            print '删除'

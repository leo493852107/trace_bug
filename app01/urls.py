#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "leo"
__time__ = "2020-04-06"

from django.urls import path

from app01.views import register

urlpatterns = [
    path('register/', register),
]

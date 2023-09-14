#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 02:08:42 2023

@author: muaz
"""

from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index")
    ]
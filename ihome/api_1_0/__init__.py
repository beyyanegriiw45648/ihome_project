# -*- coding:utf-8 -*-
from flask import Blueprint
from ihome import db

api=Blueprint("api_1_0",__name__)

from . import index
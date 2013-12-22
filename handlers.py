#!/bin/python
#-*- encoding:UTF-8 -*-

import web
from tasks import transform_task

render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()


class Transform:
    def POST(self):
        i = web.input()
        result = transform_task.delay(i.url)
        return result.get(timeout=1)


class Monitor:
    def GET(self):
        i = web.input()
        return ''


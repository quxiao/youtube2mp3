#!/bin/python
#-*- encoding:UTF-8 -*-

import logging
import web
from tasks import transform_task, celery_app

render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()


class Transform:
    def POST(self):
        i = web.input()
        result = transform_task.delay(i.url)
        logging.debug('task_id: %s', result.task_id)
        web.seeother(('/monitor?task_id=%s' % (result.task_id)))


class Monitor:
    def GET(self):
        i = web.input()
        try:
            task_id = i.task_id
        except Exception:
            #TODO
            pass

        result = transform_task.AsyncResult(task_id)
        return result.status
        celery_inspect = celery_app.control.inspect()
        return celery_inspect.active()


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
        if result.status != 'SUCCESS':
            url = ''
        else:
            url = result.get()
            url = '<a href="%s">%s</a>' % (url, url)

        logging.debug('%s, %s, %s', task_id, result.status, url)
        return render.monitor(task_id, result.status, url)
            

#custom notfound
def notfound():
    return web.notfound(render.notfound())

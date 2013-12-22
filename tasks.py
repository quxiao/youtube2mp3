#!/bin/python
#-*- encoding:UTF-8 -*-

from __future__ import absolute_import
import time
from celery import Celery


celery_app = Celery('youtube2mp3_proj',
                    broker='amqp://localhost',
                    backend='amqp://localhost')


@celery_app.task(bind=True)
def transform_task(self, youtube_url):
    for i in range(10):
        time.sleep(1)
        self.update_state(state=('state %d' % i))
        print 'hello celery: %d' % (i)
    return "hello celery :%s" % (youtube_url)


if __name__ == '__main__':
    celery_app.start()


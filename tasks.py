#!/bin/python
#-*- encoding:UTF-8 -*-

from __future__ import absolute_import
from celery import Celery


app = Celery('youtube2mp3_proj',
                    broker='amqp://localhost',
                    backend='amqp://localhost')


@app.task
def transform_task(youtube_url):
    return "hello celery :%s" % (youtube_url)


if __name__ == '__main__':
    app.start()


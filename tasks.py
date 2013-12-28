#!/bin/python
#-*- encoding:UTF-8 -*-

from __future__ import absolute_import
import time
import subprocess
from celery import Celery

DOWNLOAD_DIR = '/home/quxiao/dev/youtube2mp3/static'

celery_app = Celery('youtube2mp3_proj',
                    broker='amqp://localhost',
                    backend='amqp://localhost')


@celery_app.task(bind=True)
def transform_task(self, youtube_url):
    #get title
    self.update_state(state='Getting Title')
    proc = subprocess.Popen('youtube-dl --get-id %s' % (youtube_url), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=DOWNLOAD_DIR, shell=True)
    if proc.wait() != 0:
        return 'Cannot get title. Error!'
    title = proc.stdout.read()
    #get filename
    if len(title) == 0:
        self.update_state(state='Getting File Name')
        proc = subprocess.Popen('youtube-dl --get-filename %s' % (youtube_url), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=DOWNLOAD_DIR, shell=True)
        if proc.wait() != 0:
            return 'Cannot get filename. Error!'
        title = proc.stdout.read()
    print title

    #download and convert
    proc = subprocess.Popen('youtube-dl --newline -x --audio-format mp3 -o "%%(title)s.%%(ext)s" %s' % (youtube_url), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=DOWNLOAD_DIR, shell=True)
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        self.update_state(state=line)
        print line
    return 'static/%s.mp3' % (title)


if __name__ == '__main__':
    celery_app.start()


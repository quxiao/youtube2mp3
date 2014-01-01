#!/bin/python
#-*- encoding:UTF-8 -*-

from __future__ import absolute_import
import time
import subprocess
from celery import Celery, states

DOWNLOAD_DIR = '/home/quxiao/dev/youtube2mp3/static'

celery_app = Celery('youtube2mp3_proj',
                    broker='amqp://localhost',
                    backend='amqp://localhost')


@celery_app.task(bind=True)
def transform_task(self, youtube_url):
    #get id
    self.update_state(state='Getting File ID')
    proc = subprocess.Popen('youtube-dl --get-id %s' % (youtube_url), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=DOWNLOAD_DIR, shell=True)
    if proc.wait() != 0:
        self.update_state(state=states.FAILURE)
        return 'Cannot get filename. Error!'
    title = proc.stdout.read()
    print title

    #download and convert
    proc = subprocess.Popen('youtube-dl --no-cache-dir -r 5M --newline -x --audio-format mp3 -o "%%(id)s.%%(ext)s" %s' % (youtube_url), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=DOWNLOAD_DIR, shell=True)
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        self.update_state(state=line)
        print line
    if proc.wait() != 0:
        self.update_state(state=states.FAILURE)
        return 'Download failed!'
    return 'static/%s.mp3' % (title)


if __name__ == '__main__':
    celery_app.start()


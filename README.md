youtube2mp3
===========

A simple website for downloading youtube video and converting video to mp3

Requirements
--------------

* Python 2.7+
* Webpy Framework, see [this](http://webpy.org/install#install)
* Celery, see [this](http://www.celeryproject.org/install/)
* Youtube-dl, see [this](http://rg3.github.io/youtube-dl/download.html)
* ffmpeg, see [this](http://www.ffmpeg.org/download.html)


How to run
-------------

Put bin into local directory

    sudo cp ffmpeg /usr/local/bin/
    sudo cp youtube-dl /usr/local/bin/

Run celery server

    nohup celery -A tasks worker -l debug &

Run webpy server

    nohup python code.py 8080

the parameter means server port

Then, check url `http://your_ip_or_domain_name:port`


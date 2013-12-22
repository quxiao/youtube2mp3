#!/bin/python
#-*- encoding:UTF-8 -*-

import logging
import web
from handlers import Index, Transform, Monitor, notfound

render = web.template.render('templates')

urls = (
        '/', 'Index',
        '/transform', 'Transform',
        '/monitor', 'Monitor'
)

app = web.application(urls, globals())


if __name__ == '__main__':
    logging.basicConfig(filename="server.log", level=logging.DEBUG)
    app.notfound = notfound
    app.run()


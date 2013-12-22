#!/bin/python
#-*- encoding:UTF-8 -*-

import web
from handlers import Index, Transform

render = web.template.render('templates')

urls = (
        '/', 'Index',
        '/transform', 'Transform'
)

app = web.application(urls, globals())


if __name__ == '__main__':
    app.run()


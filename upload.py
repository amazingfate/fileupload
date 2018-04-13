#!/usr/bin/python3
# coding: utf-8

import tornado.ioloop
import tornado.web
import shutil
import os
import json
import hashlib


class FileUploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        ret = {'result': 'OK'}
        upload_path = os.path.join(os.path.dirname(__file__), 'files')
        file_metas = self.request.files.get('file', None)

        if not file_metas:
            ret['result'] = 'Invalid Args'
            return ret

        for meta in file_metas:
            filename = meta['filename']
            file_path = os.path.join(upload_path, filename)


            with open(file_path, 'wb') as up:
                up.write(meta['body'])
                # OR do other thing

        self.write(json.dumps(ret))

settings = {
    'static_path': 'js',
    'static_url_prefix': '/js/'
}

app = tornado.web.Application([
    (r'/file', FileUploadHandler),
], default_host='',transforms=None, **settings)

if __name__ == '__main__':
    app.listen(8765)
    tornado.ioloop.IOLoop.instance().start()

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
        ret = {'result': 'OK','url':''}
        upload_path = os.path.join(os.path.dirname(__file__), 'static/files')
        file_metas = self.request.files.get('file', None)

        if not file_metas:
            ret['result'] = 'Invalid Args'
            return ret

        for meta in file_metas:
            filename = meta['filename']
            image_name, image_type = filename.split('.')
            file_path = os.path.join(upload_path, filename)


            with open(file_path, 'wb') as up:
                up.write(meta['body'])

            image_file = open(file_path,'rb')
            image_file_data = image_file.read(4096)
            image_file.close()
            image_file_md5 = hashlib.md5(image_file_data)
            image_file_md5value = image_file_md5.hexdigest()
            new_image_name = image_file_md5value + '.' + image_type
            image_path = os.path.join(upload_path,new_image_name)
            shutil.move(file_path, image_path)
            ret['url'] = 'http://10.90.79.233:8765/static/files/' + new_image_name

        self.write(json.dumps(ret))

settings = {
    'static_path': 'static',
    'static_url_prefix': '/static/'
}

app = tornado.web.Application([
    (r'/file', FileUploadHandler),
], default_host='',transforms=None, **settings)

if __name__ == '__main__':
    app.listen(8765)
    tornado.ioloop.IOLoop.instance().start()

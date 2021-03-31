#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author: kzaopa

import time
import urlparse
from pocsuite.api.request import req
from pocsuite.api.poc import register
from pocsuite.api.poc import Output, POCBase

class TestPOC(POCBase):
    vulID = '1'
    version = '1'
    author = ''
    vulDate = '2018-09-29'
    createDate = '2018-09-29'
    updateDate = '2018-09-29'
    references = [
        'Null',
    ]
    name = 'url_check'
    appPowerLink = 'Null'
    appName = 'Null'
    appVersion = ''
    vulType = 'url_check'
    desc = '''
    url_check 
    '''
    samples = []
    fn = str(int(round(time.time()*1000)))

    def _verify(self):
        result = {}
        # ports = [8080, 443]
        ports = [80]
        parse = urlparse.urlparse(self.url)
        port = parse.port
        host = parse.hostname
        scheme = parse.scheme
        if port not in ports:
            ports.append(port)
        for port in ports:
            url = '{0}://{1}:{2}'.format(scheme, host, port)
            # print url
            try:
                status = req.get(url, timeout=10)
                http_code = status.status_code
            except:
                http_code = ''
            if http_code == 200 or http_code == 500 or http_code == 404 or http_code == 403 or http_code == 302:
                with open(self.fn+'.txt', 'a') as w:
                    w.write(url+'\n')


register(TestPOC)

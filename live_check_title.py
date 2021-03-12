#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author: kzaopa

import urlparse, time, re
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
        url = self.url.split('//')[1]
        target = 'http://'+url.split(':')[0]+':'+url.split(':')[1]
        result = {}
        # ports = [80, 443]
        # parse = urlparse.urlparse(target)
        # port = parse.port
        # host = parse.hostname
        # scheme = parse.scheme
        # if port not in ports:
        #     ports.append(port)
        # for port in ports:
        # url = '{0}://{1}:{2}'.format('http', host, port)
        try:
            status = req.get(target, timeout=10)
            http_code = status.status_code
        except:
            http_code = ''
        try:
            title=re.findall('<title>(.+)</title>',status.content)[0]
        except:
            title = ''
        if http_code == 200 or http_code == 500 or http_code == 404 or http_code == 403 or http_code == 302:
            with open(self.fn+'.txt', 'a') as w:
                w.write(url+':'+title+'\n')
        else:
            with open(self.fn+'.txt', 'a') as w:
                w.write(url+':'+'\n')

register(TestPOC)

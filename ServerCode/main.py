#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from bs4 import BeautifulSoup
import urllib2
import re

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class MLH(webapp2.RequestHandler):
    def get(self):
        body = ""
        url = "https://mlh.io/seasons/s2016/events"
        response = urllib2.urlopen(url)
        data = response.read()
        arr = data.split('event-wrapper">', 1)
        data = arr[1]
        arr2 = data.split('<h4>')
        data = arr2[0]
        self.response.write(data)
        soup = BeautifulSoup(data, "html.parser")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/mlh', MLH),
], debug=True)






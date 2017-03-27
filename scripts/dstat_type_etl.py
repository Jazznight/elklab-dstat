#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin, stdout, stderr
import os, time, traceback
import json


class Event(dict):
    def __init__(self, data):
        super(Event, self).__init__(data)

    def to_int(self):
        for k in self['dstat']:
            for sk in self['dstat'][k]:
              self['dstat'][k][sk] = float(self['dstat'][k][sk])


while True:
    try:
        raw = stdin.readline().strip()
        data = json.loads(raw)

        event = Event(data)
        event.to_int()

        stdout.write(json.dumps(event))
        stdout.flush()
    except Exception as e:
        stderr.write( "\n[ERROR] <%s>\n"%(e.args[0]) )
        #stderr.write( "[ERROR_DATA] <%s>\n\n"%(str(data)) )
        traceback.print_exc()
        stderr.flush()
        pass

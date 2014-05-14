#!/usr/bin/env python
import sys
import pytz
import re
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_timezones(partial):
    regex = re.compile(re.escape(partial.lower()))
    for timezone in pytz.all_timezones:
        if re.search(regex, timezone.lower()):
            yield timezone


def run(partial):
    for timezone in get_timezones(partial):
        tz = pytz.timezone(timezone)
        print datetime.now(tz).strftime(DATE_FORMAT), timezone

if len(sys.argv) == 1:
    print "Usage: world-clock <timezone>"
    print
    print "world-clock matches the entered timezone against \
a list of all timezones and prints the local time \
in all of them"
else:
    run(sys.argv[1])

#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print "Usage: %s <file>" % sys.argv[0]
    exit(1)

fn = sys.argv[1]

prev = ""
with open(fn, 'read') as f:
    for ln, l in enumerate(f):
        stripped = l.strip()
        if stripped == "\\iffalse":
            if prev != "" and prev != "\\fi":
                print "%s Line %d: Extra \\iffalse!" % (fn, ln)
            prev = "\\iffalse"
        elif stripped == "\\fi":
            if prev != "\\iffalse":
                print "%s Line %d: Extra \\fi!" % (fn, ln)
            prev = "\\fi"


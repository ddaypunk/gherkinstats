__author__ = 'andydelso'

# from gherkin import Gherkin
import sys
import re

tags = []
feature = []
background = []
scenarios = []

#regular expressions
tags_re = re.compile("\@[a-z|A-Z]*")
feature_re = re.compile()

f = open(sys.argv[1], mode='r')

all_lines = f.readlines()

for line in all_lines:
    pre_tags = tags_re.findall(line)
    if pre_tags:
        tags = pre_tags

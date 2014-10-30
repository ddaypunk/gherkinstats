__author__ = 'andydelso'

# from gherkin import Gherkin
import sys
import re

tags = []
feature = []
background = []
scenarios = []

f = open(sys.argv[1], mode='r')

all_lines = f.readlines()

for line in all_lines:
    if re.search('\@.'):
        tags.append()
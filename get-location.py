#!/usr/bin/env python3

import sys

_, ip = sys.argv
for line in sys.stdin:
    if line == '\n':
        continue
    line = line.rstrip()
    if line[0] == line[1] == '\t':
        constraint = line
        if ip in constraint:
            city = city.split('(')[0].strip()
            country = country.split('(')[0].strip()
            print(f'{city}, {country}')
            break
    elif line[0] == '\t':
        city = line
    else:
        country = line

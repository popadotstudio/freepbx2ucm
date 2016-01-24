#!/usr/bin/python3

# This little script takes a regular exported CSV from the UCM software and helps build the master templates faster
#
# The script will read the CSV's file HEADER and 1ST ROW only. So as a requirement we will need that first extension to
# be added as a sample extension, with most parameters left as Grandstream wanted them to be as default.


# By default we load 'export_sip_extensions.csv' from the current directory because that is the default name exported
with open('export_sip_extensions.csv') as datafile:
    columns = datafile.readline().split(',')
    values = datafile.readline().split(',')

# Mappings Template
print('mappings_template = {')
firstline = True
for c,v in zip(columns, values):
    if firstline:
        firstline = False
        c = c[1:] # keep it simple stupid :D
    print('    {c:45}: "{v}",'.format(c='"'+c.strip()+'"', pad=" ", v=v.strip()))
print('}')

# Header List (because dicts in python are not ordered and using an OrderedDict isn't pretty enough .. are you listening
# Python Gods? :D)

print()
print('mappings_header = [', end="")
firstline = True
for c in columns:
    if firstline:
        firstline = False
        c = c[1:] # keep it simple stupid :D
    print('"%s", ' % c.strip(), end="")
print(']')

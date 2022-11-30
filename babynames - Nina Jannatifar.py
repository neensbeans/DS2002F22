#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Baby Names Exercise Part A

1. Define the extract_names() function below and change main() to call it.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

2. Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

import sys
import re

# 1. set up the names list that will eventually be returned 
names = []

# 2. set up extract_names function
def extract_names(filename):
    # open and create the HTML file
    f = open(filename, 'r')
    nameData = f.read
    
    # determine the year in the file -> format of the line containing the year is "Popularity in yyyy"
    find_year = re.search(r'Popularity\sin\s(\d\d\d\d)')
    # re.search() is used to parse: \s indicates a space and \d is any Unicode decimal digit
    # in case the year is not found in the file, throw an error
    if not find_year:
        sys.exit('Year not found!')
    year = find_year.group(1) 
    # .group(1) pulls the first value in the parenthesis -> (\d\d\d\d)
    names.append(year)
    # adds the year to the currently empty names list 
    
# 3. prepare the data tuples -> (rank)(boy's name)(girl's name)
    dataGroups = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', nameData)
    #(\d+ -> matches 1+ digits) (\w+ -> match 1+ char)

# 4. for each tuple, unpack the three variables into a new dict
    rankedNames = {}
    for rank, boyName, girlName in dataGroups:
        if boyname not in rankedNames:
          rankedNames[boyName] = rank
        if girlname not in rankedNames:
          rankedNames[girlName] = rank
# 5. created the sorted list
sortedNames = sorted(rankedNames.keys()) # sorted default is ascending order

#6. add elements to the names list
for name in sortedNames:
    names.append(name + " " + rankedNames[name])
return names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  for filename in args:
    names = extract_names(filename)

    # Make text out of the whole list
    text ='\n'.join(names) + '\n' #provided in directions
print text


if __name__ == '__main__':
  main()


# In[ ]:





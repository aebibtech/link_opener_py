# Author: Paul Abib Camano
# This module contains functions that
# operate on text files for extracting
#
# This can work as a standalone program. It opens links in the browser.

# import os
import webbrowser
import sys
from tkinter import filedialog

# This function gets the Youtube Links from a file
# returns a list
def get_links(file):
    links = []
    for line in file:
        if line.startswith("https://"):
            lnk = line.replace('\n', '') # Strip \n from link
            print('Link found: ', lnk)
            links.append(lnk)
    return links


fi = None
fhand = None
try:
    fi = sys.argv[1]
    fhand = open(fi, 'r')
except:
    fhand = filedialog.askopenfile('r')


if fhand == None:
    sys.exit('No file selected.')
links = get_links(fhand)

count = 0
for link in links:
    if count == 0:
        webbrowser.open(link, 1)
    else:
        webbrowser.open(link, 2)



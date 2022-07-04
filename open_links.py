# Author: Paul Abib Camano
# This module contains functions that
# operate on text files for extracting
# YouTube links.
#
# This can work as a standalone program. It opens links in the browser.
# For now, it works on Windows. 

import os
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


# This function opens Google Chrome with the Link Specified.
# win_type - "w" for New Window, "t" for New Tab
def chrome(link = "https://www.google.com", win_type = "w"):
    gc_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    wtype = None
    if win_type == 'w':
        wtype = '--new-window'
    elif win_type == 't':
        wtype = '--new-tab'
    os.system("\"{}\" {} {}".format(gc_path, wtype, link))


fi = None
fhand = None
try:
    fi = sys.argv[1]
    fhand = open(fi, 'r')
except:
    fhand = filedialog.askopenfile('r')


if fhand == None:
    exit()
links = get_links(fhand)

count = 0
for link in links:
    if count == 0:
        chrome(link)
    else:
        chrome(link,'t')
    count += 1
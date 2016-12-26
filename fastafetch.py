#!/usr/bin/python
"""
This script fetches fasta files from uniprot.org for all proteins in a csv file.
UniProt IDs should be listed in the first column of the csv under a header.
Created 12/25/2016
@author: Christine Yao-yun Chang
"""

import sys
import csv
import requests
import time
import os

start_time = time.clock() #timer

#hardcoded file access
#with open("/location/of/prot_list.csv", "r") as infile:

#user customized parsing
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Please define input file and output location (default here).")
    print("Syntax: python fastafetch.py inputfile.csv /path/to/output")
    sys.exit()

prot_list = sys.argv[1]
if len(sys.argv) == 3:
    output = sys.argv[2] #define an output location
else:
    output = os.getcwd() #else fasta files will be stored in current working directory

#check prot_list for queries in Uniprot_ID column (column 0)
with open(prot_list, "r") as infile:
    reader = csv.reader(infile)
    next(reader, None) #skip headers
    for row in reader:
        protID = row[0]
        url = 'http://www.uniprot.org/uniprot/' + protID +'.fasta' #build url of fasta file from uniprot.org
        #print("Gathering: ", url) #see what you pulled out
        response = requests.get(url)
        loc = output + "\\" + protID + '.fasta' #save fasta files locally
        with open(loc, 'wb') as f:
            f.write(response.content)

print("---%s seconds---" % (time.clock() - start_time))

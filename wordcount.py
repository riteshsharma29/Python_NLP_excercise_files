#! /usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from bs4 import BeautifulSoup
import urllib2
from nltk.corpus import stopwords
import sys

#to switch system's default encoding to 'utf-8'

reload(sys)
sys.setdefaultencoding("utf-8")

class Wordcount():

    def __init__(self,url,sample):

       #webpage url is the url link to be read, int value for number of samples

        self.url = url
        self.sample = sample

    def plot_wc(self):

        #method to read the draw a plot for frequency of repeated word in a webpage

        html = urllib2.urlopen(self.url).read()
        soup = BeautifulSoup(html,"html5lib")
        text = soup.get_text(strip=True)
          
        #List comprehension   
 
        tokens = [t for t in text.split()]
        clean_tokens = tokens[:] 

        #uncomment below code for downloading stopwords list using below method if required 
        #nltk.download('stopwords')

        for token in tokens: 
        #any token found in stopwords.word english dictionary will be removed
            if token in stopwords.words('english'): 
                clean_tokens.remove(token) 
        freq = nltk.FreqDist(clean_tokens) 
        freq.plot(self.sample,cumulative=False)
        for key,val in freq.items(): 
            print (str(key).encode('utf-8') + ':' + str(val).encode('utf-8'))



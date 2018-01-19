#! /usr/bin/env python
# -*- coding: utf-8 -*-

import wordcount

#creating instance of an object, Read below URL html pagesource with 10 sample values

url_1 = wordcount.Wordcount("http://php.net/",10)

#Plot a graph showing the count word frequency in the webpage results

url_1.plot_wc()


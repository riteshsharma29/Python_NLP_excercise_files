#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Tokenization process ie Splitting Bigger parts to smaller parts

from nltk.tokenize import sent_tokenize 
from nltk.tokenize import word_tokenize
import sys
import pandas as pd

mystring = "Pandas is also compatible with many of the other data analysis libraries, like Scikit-Learn for machine learning, Matplotlib for Graphing, NumPy, since it uses NumPy, and more. It's incredibly powerful and valuable to know. If you're someone who finds themselves using Excel, or general spreadsheets, for various computational tasks, where they might take a minute, or an hour, to run, Pandas is going to change your life. I've even seen versions of Machine learning like K-Means clustering being done on Excel. That's really cool, but my Python is going to do that for you way faster, which will also allow you to be a bit more stringent on parameters, have larger datasets and just plain get more done."

sentc = sent_tokenize(mystring)

wrds = word_tokenize(mystring)

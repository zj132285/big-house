# -*- coding: utf-8 -*-

from snownlp import SnowNLP  
text = raw_input('input your sentence,in Chinese please: ')
s = SnowNLP(text)
    
class SentimentStr():
    x = s.sentiments
    if x > 0.5:
        print 'it tends to be positive'
    if x == 0.5:
        print 'it tends to be neutral'
    if x < 0.5:
        print 'it tends to be negative'
    print x
  



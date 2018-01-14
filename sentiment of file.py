# -*- coding: utf-8 -*-

from snownlp import SnowNLP  
import xlrd
data = xlrd.open_workbook('/Users/jay/desktop/wenjian/xbf1.xlsx')

table = data.sheets()[0] 
nrows = table.nrows
for i in range(nrows): 
    s = SnowNLP (str(table.row_values(i)).decode("unicode_escape").encode("utf8"))
    x = s.sentiments
    if x > 0.5:
        print 'it tends to be positive'
    if x == 0.5:
        print 'it tends to be neutral'
    if x < 0.5:
        print 'it tends to be negative'


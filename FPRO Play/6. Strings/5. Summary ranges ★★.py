# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 15:01:03 2018

@author: diogo
"""

def summary_ranges(astring):
    numlist = astring.split(",")
    count = 0
    result_list = []
    result = ""
    
    for i in range(int(numlist[len(numlist)-1])+1):
        if str(i) in numlist:
            count = count + 1
            if str(i+1) not in numlist:
                if count == 1:
                    result_list += [str(i)]
                    count = 0
                else:
                    result_list += [str(i-count+1) + "->" + str(i)]
                    count = 0
    result = ",".join(result_list)
    
    return result

print(summary_ranges("0,1,2,3,4,5,7,10,11,20,21"))
print(summary_ranges("1,3,4,6,7,9,10"))
    
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:29:06 2018

@author: diogo
"""

def manipulator(l,cmds):
    final_result = ""
    for i in range(len(cmds)):  
        
        if cmds[i][:6] == "insert":
            a = cmds[i].split()           
            result = l.insert(int(a[1]),int(a[2]))

        if cmds[i][:5] == "print":
            result = str(l)
            final_result = final_result + result + " "
            
        if cmds[i][:6] == "remove":
            a = cmds[i].split()
            result = l.remove(int(a[1]))

        if cmds[i][:6] == "append":
            a = cmds[i].split()
            result = l.append(int(a[1]))

        if cmds[i][:4] == "sort":
            result = l.sort()

        if cmds[i][:3] == "pop":
            result = l.pop()

        if cmds[i][:7] == "reverse":
            result = l.reverse()
            
    return final_result

print(manipulator([], ["insert 0 5",
                  "insert 1 10", 
                  "insert 0 6",
                  "print", 
                  "remove 6", 
                  "append 9", 
                  "append 1", 
                  "sort", 
                  "print",
                  "pop", 
                  "reverse", 
                  "print"]))
    
print(manipulator([2, 4], ["print", 
                          "remove 4", 
                          "append 1", 
                          "sort", 
                          "print", 
                          "pop", 
                          "reverse", 
                          "print"]))
    
print(manipulator([], ["print"]))
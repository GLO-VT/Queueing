# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:14:01 2018

@author: Bobby
Queue for use with SSTracking
"""
import queue

#size of queue(s)
#SS1
SS1X = queue.Queue(maxsize=1) 
SS1Y = queue.Queue(maxsize=1) 
SS1time = queue.Queue(maxsize=1)
#SS2
SS2X = queue.Queue(maxsize=1)
SS2Y = queue.Queue(maxsize=1)
SS2time= queue.Queue(maxsize=1)
 #SS3
SS3X = queue.Queue(maxsize=1) 
SS3Y = queue.Queue(maxsize=1) 
SS3time = queue.Queue(maxsize=1) 
#Queue
#Use care, queuing to full queue causes infinite loop
#Use classes from GLO_tracking for data to queue
if(SS1X.full()==False):
    SS1X.put(1)
if(SS1Y.full()==False):
    SS1Y.put(2)
if(SS1time.full()==False):
    SS1time.put("HH:MM:SS")
if(SS2X.full()==False):    
    SS2X.put(3)
if(SS2Y.full()==False):
    SS2Y.put(4)
if(SS2time.full()==False):
    SS2time.put("HH:MM:SS")
if(SS3X.full()==False):
    SS3X.put(5)
if(SS3Y.full()==False):
    SS3Y.put(6)
if(SS3time.full()==False):
    SS3time.put("HH:MM:SS")
#DeQueue 
#Use care, dequeuing empty queue causes infinite loop
#Instead of printing, use classes from GLO_Tracking for data
if(SS1X.empty()==False):
    print(SS1X.get())
if(SS1Y.empty()==False):
    print(SS1Y.get())
if(SS1time.empty()==False):
    print(SS1time.get())
if(SS2X.empty()==False):
    print(SS2X.get())
if(SS2Y.empty()==False):
    print(SS2Y.get())
if(SS2time.empty()==False):
    print(SS2time.get())
if(SS3X.empty()==False):
    print(SS3X.get())
if(SS3Y.empty()==False):
    print(SS3Y.get())
if(SS3time.empty()==False):
    print(SS3time.get())


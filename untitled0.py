# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:00:06 2017

@author: ldn
"""
EndPointCoordinate=((-3.6,0.0,7.355),(123.6,0.0,7.355))    #west & east end point
rGirderRigidarmCoordinate=((10,8.13,0),(15,8.3675,0),(20,8.58,0),
    (25,8.7675,0),(30,8.93,0),(35,9.0675,0),(40,9.18,0),(45,9.2675,0),(50,9.33,0),(55,9.3675,0),
    (60,9.38,0),
    (65,9.3675,0),(70,9.33,0),(75,9.2675,0),(80,9.18,0),(85,9.0675,0),(90,8.93,0),(95,8.7675,0),
    (100,8.58,0),(105,8.3675,0),(110,8.13,0))

rRigidarmSuspenderCoordinate=(((10,7.73,-3.75),(15,7.9675,-3.75),(20,8.18,-3.75),
    (30,8.53,-3.75),(35,8.6675,-3.75),(40,8.78,-3.75),(45,8.8675,-3.75),(50,8.93,-3.75),(55,8.9675,-3.75),
    (60,8.98,-3.75),
    (65,8.9675,-3.75),(70,8.93,-3.75),(75,8.8675,-3.75),(80,8.78,-3.75),(85,8.6675,-3.75),(90,8.53,-3.75),
    (100,8.18,-3.75),(105,7.9675,-3.75),(110,7.73,-3.75)),

    ((10,7.73,3.75),(15,7.9675,3.75),(20,8.18,3.75),
    (30,8.53,3.75),(35,8.6675,3.75),(40,8.78,3.75),(45,8.8675,3.75),(50,8.93,3.75),(55,8.9675,3.75),
    (60,8.98,3.75),
    (65,8.9675,3.75),(70,8.93,3.75),(75,8.8675,3.75),(80,8.78,3.75),(85,8.6675,3.75),(90,8.53,3.75),
    (100,8.18,3.75),(105,7.9675,3.75),(110,7.73,3.75)))

lst=[]
lst.append(EndPointCoordinate[0])
for i in range(len(rGirderRigidarmCoordinate)):
    lst.append(rGirderRigidarmCoordinate[i])
lst.append(EndPointCoordinate[1])
l=tuple(lst)
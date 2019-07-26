def find_anthill_order(i):
    anthills=[]
    for j in i:
        if j[1:3]==['0','0']:
            anthills.append('AH0')
        elif j[1:3]==['0','1']:
            anthills.append('AH1')
        elif j[1:3]==['1','0']:
            anthills.append('AH2')
        else:
            anthills.append('AH3')
    return anthills
            

def find_queen_anthill(i,order):
    for j in range(4):
        if i[j][0]==str(1):
            return order[j]

def find_thrash(i,order):
    T=[]
    for j in range(4):
        if i[j][7]==str(1):
            T.append(order[j])
    return T

def find_services(i,order):
    S={}
    for j in range(4):
        service=[]
        if i[j][5:7]==['0','0']:
            service.append('No supply')
        elif i[j][5:7]==['0','1']:
            service.append('Honey dew')
        elif i[j][5:7]==['1','0']:
            service.append('Leaves')
        else:
            service.append('Wood')
        if i[j][3:5]==['0','0']:
            service.append('No supply')
        elif i[j][3:5]==['0','1']:
            service.append('Honey dew')
        elif i[j][3:5]==['1','0']:
            service.append('Leaves')
        else:
            service.append('Wood')
        S[order[j]]=service
    return S
        
    
        

import cv2
import numpy as np
import time
import cv2.aruco as aruco

image=cv2.imread('aruco_markers.jpg')
idlist=[]
binary_idlist=[]
run =True

while run:
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)             #converting to grayscale
    aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_1000)     #defining the dictionary in which the ids are present

    parameters = aruco.DetectorParameters_create()             #finding the parameters
    corners, ids, _ = aruco.detectMarkers(image,aruco_dict , parameters = parameters)
    if len(corners):
        for i in range(len(corners)):
            if ids[i][0] not in idlist:
                idlist.append(ids[i][0])    #appending the detected ids to the final list
                if len(idlist) == 4:
                    run=False
                    
for i in idlist:
    temp1=str(bin(i))
    binary_id=temp1[2:]
    temp2=list(binary_id)
    flag=False
    if (len(temp2)<8):
        flag=True
    while(flag):
        if (len(temp2)<8):
            temp2=['0']+temp2
            
        else:
            flag=False
    binary_idlist.append(list(temp2))

print('idlist=',idlist)
print('binary id list=',binary_idlist)
anthill_order=find_anthill_order(binary_idlist)
print('anthill order=',anthill_order)
queen_anthill=find_queen_anthill(binary_idlist,anthill_order)
print('queen anthill=',queen_anthill)
thrash=find_thrash(binary_idlist,anthill_order)
print('thrash list',thrash)
service=find_services(binary_idlist,anthill_order)
print('services=',service)


    


#cv2.imshow('image',image)
#cv2.imshow('gray',gray)
cv2.waitKey(10000)
cv2.destroyAllWindows()

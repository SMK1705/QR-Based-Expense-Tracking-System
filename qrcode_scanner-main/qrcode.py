import cv2
import numpy as np
from pyzbar.pyzbar import decode
#from pyzbar.pyzbar import ZBarSymbol


a = open("C:\\SMK\\DA\\Python\\Project\\QR\\Dat\\a.txt",'w+')

cap = cv2.VideoCapture(0)
cap.set(3,640) #width of the frames in the video feed
cap.set(4,480) #height of the frames in the video feed 
i=0
b=[]

while len(b)<1:
    ret,img = cap.read()
    cv2.imshow('answer',img)
    for barcode in decode(img):
        mydata = barcode.data.decode('utf-8')
        myd=mydata.split(",")
        print(myd)
        b.append(myd)
        
    cv2.waitKey(1)

#print(b)
cv2.destroyAllWindows()

for i in range(1):
     a.write(str(b))

l=[]
l=b[0].split()

res_str = [ele for ele in l if isinstance(ele, str)]
res_int = [ele for ele in l if isinstance(ele, int)]

#print(b)

print(str(res_int))
print(str(res_str))


grocery = [ 'supermarket','food','market','delicatessen','hypermarket','greengrocery','pharmacy',
            'grocery','store','greengrocer','general store','convenience store','walmart','mart	shop',
            'grocer store','cashier','shopper','dairy','pizza','warehouse','mall','restaurants','marketplace','retailer']

if str(res_str) in grocery:
    print(str(res_str))





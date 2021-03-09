import cv2
import numpy as np
import os

img_path='./img/'
txt_path='./save_txt/'
save_img_path='./save_img/'

for img_file in os.listdir(img_path):
    image = cv2.imread(img_path+img_file,1)
    #print(img_file[:-4])
    with open(txt_path+img_file[:-4]+'.txt','r') as f:
        lines=f.readlines()
        for line in lines:
            line.strip()
            words=line.split(',')
            points=np.array([[words[0],words[1]],[words[2],words[3]],[words[4],words[5]],[words[6],words[7]]],np.int32)

            #points=np.array([[150,50],[140,140],[200,170],[250,250]],np.int32)
            cv2.polylines(image,[points],True,(0,0,255))

    #cv2.imshow('image',image)
    #cv2.waitKey()
    cv2.imwrite(save_img_path+'p_'+img_file,image)

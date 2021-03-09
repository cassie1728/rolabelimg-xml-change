# coding=utf-8
# 读xml文件中的一个rect
import xml.etree.ElementTree as ET
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

import math
import numpy as np
'''
def rect_loc(row, col, angle, height, bottom):
    #print(angle)
    #angle=round(float(angle), 2)
    assert angle <= 180, 'angle out of index'
    #angle *= (10 / 180) * math.pi
    angle=(-1)*math.radians(angle)

    xo = np.cos(angle)
    yo = np.sin(angle)

    y1 = row + height / 2 * yo
    x1 = col - height / 2 * xo
    y2 = row - height / 2 * yo
    x2 = col + height / 2 * xo
    
    return np.array(
        [
         [y1 - bottom/2 * xo, x1 - bottom/2 * yo],
         [y2 - bottom/2 * xo, x2 - bottom/2 * yo],
         [y2 + bottom/2 * xo, x2 + bottom/2 * yo],
         [y1 + bottom/2 * xo, x1 + bottom/2 * yo],
         ]
    ).astype(np.int)
    
    return [int(y1 - bottom/2 * xo),int(x1 - bottom/2 * yo),int(y1 + bottom/2 * xo),int(x1 + bottom/2 * yo),int(y2 + bottom/2 * xo),int(x2 + bottom/2 * yo),int(y2 - bottom/2 * xo),int(x2 - bottom/2 * yo)]
'''
def rotatePoint(xc,yc, xp,yp, theta):
    xoff = xp-xc;
    yoff = yp-yc;        
    cosTheta = math.cos(theta)
    sinTheta = math.sin(theta)
    pResx = cosTheta * xoff + sinTheta * yoff
    pResy = - sinTheta * xoff + cosTheta * yoff
    # pRes = (xc + pResx, yc + pResy)
    return xc+pResx,yc+pResy

def addRotatedShape(cx,cy,w,h,angle): 
    p0x,p0y = rotatePoint(cx,cy, cx - w/2, cy - h/2, -angle)
    p1x,p1y = rotatePoint(cx,cy, cx + w/2, cy - h/2, -angle)
    p2x,p2y = rotatePoint(cx,cy, cx + w/2, cy + h/2, -angle)
    p3x,p3y = rotatePoint(cx,cy, cx - w/2, cy + h/2, -angle)
    points = [p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y]
    return points

xml_path='./xml/'
save_xml_path='./save_txt/'
for xml_file in os.listdir(xml_path):
    #xml_path='/Users/zhangjiaxuan/Desktop/change_test/xml/IMG_6550.xml'
    tree = ET.parse(xml_path+xml_file)
    rect={}
    line=""
    root = tree.getroot()
    for name in root.iter('path'):
        rect['path'] = name.text
    for ob in root.iter('object'):
        #print(ob.iter('bndbox'))
        #print(ob.find('type').text)
        if ob.find('bndbox') is not None:
            for bndbox in ob.iter('bndbox'):
                # for l in bndbox:
                #     print(l.text)
                for xmin in bndbox.iter('xmin'):
                    rect['xmin'] = xmin.text
                for ymin in bndbox.iter('ymin'):
                    rect['ymin'] = ymin.text
                for xmax in bndbox.iter('xmax'):
                    rect['xmax'] = xmax.text
                for ymax in bndbox.iter('ymax'):
                    rect['ymax'] = ymax.text
 
            line = rect['path'] + "\t"+ rect['xmin']+ "\t"+rect['ymin']+"\t"+rect['xmax']+"\t"+rect['ymax']+'\n'
        
            #f1 = open('./IMG_6550_all.txt', 'a')
            #f1.write(line)

            line2 = rect['xmin']+ ","+rect['ymin']+","+rect['xmax']+","+rect['ymin']+','+rect['xmax']+','+rect['ymax']+','+rect['xmin']+','+rect['ymax']+','+'textline'+'\n'
            f2 = open(save_xml_path+xml_file[:-4]+'.txt','a')
            f2.write(line2)


        if ob.find('robndbox') is not None:
            for robndbox in ob.iter('robndbox'):
                # for l in bndbox:
                #     print(l.text)
                for cx in robndbox.iter('cx'):
                    rect['cx'] = cx.text
                for cy in robndbox.iter('cy'):
                    rect['cy'] = cy.text
                for w in robndbox.iter('w'):
                    rect['w'] = w.text
                for h in robndbox.iter('h'):
                    rect['h'] = h.text
                for angle in robndbox.iter('angle'):
                    rect['angle'] = angle.text
            line = rect['path'] + "\t"+ rect['cx']+ "\t"+rect['cy']+'\t'+rect['angle']+"\t"+rect['w']+"\t"+rect['h']+'\n'

            #f1 = open(save_xml_path+'./IMG_6550_all.txt', 'a')
            #f1.write(line)

            #ro=rect_loc(float(rect['cx']),float(rect['cy']),float(rect['angle']),float(rect['h']),float(rect['w']))
            ro = addRotatedShape(float(rect['cx']),float(rect['cy']),float(rect['w']),float(rect['h']),float(rect['angle']))
            #line2 = str(ro[0])+','+ str(ro[1])+','+ str(ro[2])+','+ str(ro[3])+','+ str(ro[4])+','+ str(ro[5])+','+ str(ro[6])+','+ str(ro[7])+','+'textline'+'\n'
            line2 = str(int(ro[0]))+','+ str(int(ro[1]))+','+ str(int(ro[2]))+','+ str(int(ro[3]))+','+ str(int(ro[4]))+','+ str(int(ro[5]))+','+ str(int(ro[6]))+','+ str(int(ro[7]))+','+'textline'+'\n'
            f2 = open(save_xml_path+xml_file[:-4]+'.txt','a')
            f2.write(line2)








# coding=utf-8
# 读xml文件中的一个rect
import xml.etree.ElementTree as ET
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

xml_path='/Users/zhangjiaxuan/Desktop/change_test/xml/IMG_6550.xml'
tree = ET.parse(xml_path)
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
        f1 = open('./IMG_6550_all.txt', 'a')
        f1.write(line)
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

        f1 = open('./IMG_6550_all.txt', 'a')
        f1.write(line)
        
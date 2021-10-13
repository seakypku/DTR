import cv2
import pytesseract
from pytesseract import Output
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np


data = {}
pic = '4.png'
d = pytesseract.image_to_data(pic,output_type=Output.DICT,lang='chi_tra')
f = pytesseract.image_to_string(pic,lang='chi_tra')
im = "123"
print(d)
print(f)
for i in range(len(d['text'])):
    if len(d['text'][i]) > 0 :
        (x,y,w,h) = (d['left'][i],d['top'][i],d['width'][i],d['height'][i])
        data[d['text'][i]] = (d['left'][i],d['top'][i],d['width'][i],d['height'][i])
        cv2.rectangle(im ,(x,y) , (x+w,y+h),(255,0,0),1)

        pilimg = Image.fromarray(im)
        draw = ImageDraw.Draw(pilimg)

        font = ImageFont.truetype('simhei.ttf',15,encoding='utf-8')
        draw.text((x,y-10),d['text'][i],(255,0,0),font=font)
        im = cv2.cvtColor(np.array(pilimg),cv2.COLOR_RGB2BGR)
        print(im)

cv2.imshow('recoText',im)




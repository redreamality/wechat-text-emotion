# -*- coding: utf-8 -*-
import os,sys,locale
from PIL import Image, ImageFont, ImageDraw
  
zihao = 100
img = Image.open('1.gif')
transparency = img.info['transparency']
text = input('请输入需要转化的文字：\n')
fn = text.split('//')[0]
text = '\n'.join(text.split('//'))
im = Image.new("RGBA", (zihao*len(text) , zihao + 30), (0, 0, 0))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype(os.path.join("fonts", "C:/Windows/Fonts/冬青黑体W3.otf"), zihao) #华文中宋字体
x=1
y=1
textcolor = '#111'
shadowcolor = '#fff'
# # thin border
# dr.text((x-1, y), text, font=font, fill=shadowcolor)
# dr.text((x+1, y), text, font=font, fill=shadowcolor)
# dr.text((x, y-1), text, font=font, fill=shadowcolor)
# dr.text((x, y+1), text, font=font, fill=shadowcolor)

# # thicker border
# dr.text((x-1, y-1), text, font=font, fill=shadowcolor)
# dr.text((x+1, y-1), text, font=font, fill=shadowcolor)
# dr.text((x-1, y+1), text, font=font, fill=shadowcolor)
# dr.text((x+1, y+1), text, font=font, fill=shadowcolor)

#draw text
dr.text((x, y), text, font=font, fill=textcolor)



im.save(fn + ".gif",transparency=transparency)
# input(u'表情已生成，任意键结束！')

os.system('echo {0}.gif|fclip'.format(fn)) # c# program at C:\Users\RDT\Documents\home\projects\windows-util\File2Cilp\File2Cilp\bin\Release
print(' sent to clipboard')
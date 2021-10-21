from PIL import Image
from numpy import *

# create x and y components of Arnold's cat mapping
def iart(N):
   # 返回網格大小為length(N)×length(N)的方形網格坐標。
   y,x = meshgrid(range(N),range(N)) #注意x,y要調換!!!
   # xmap,ymap 為轉換後的座標位置
   xmap = (x+y) % N
   ymap = (x+2*y) % N
   return xmap, ymap

def art(N):
   # 返回網格大小為length(N)×length(N)的方形網格坐標。
   y,x = meshgrid(range(N),range(N)) #注意x,y要調換!!!
   # xmap,ymap 為轉換後的座標位置
   xmap = (2*x-y) % N
   ymap = (-x+y) % N
   return xmap, ymap

def findP(im_name, artLabel, p):
   # load image
   # im = array(Image.open("img_ENC\\"+im_name))
   im = array(Image.open(im_name))
   origin_im = im

   N = im.shape[0]
   
   if artLabel=="-": #反向
      xmap, ymap = art(N)
   else:
      xmap, ymap = iart(N)

   for i in range(1,2*N+1):
      # 經座標位置轉換後
      im = im[xmap,ymap]
      # 確認是否到testing period
      if i == p:
         result = Image.fromarray(im)
         # result.save("img_DEC\ART{}{}_{}".format(artLabel,p,im_name))
         result.save("DEC_ART{}{}_{}".format(artLabel,p,im_name))
         break 

# 讀檔
with open("ART-DEC-input08.txt","r") as f:
   txt = f.readlines()

output_txt = []
for t in txt:
   t = t.split()
   # 0:image name, 1:art(+) or iart(-), 2:The period P needed for the test image
   print(t[0], t[1], t[2])
   findP(t[0], t[1], int(t[2]))
   print(t[0].split('_')[1])
   output_txt.append(t[0].split('_')[1]+'\n')

# 寫檔
with open("ART-DEC-output08.txt","w") as f:
   for t in output_txt:
      f.write(t)
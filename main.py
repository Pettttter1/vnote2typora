import io
import sys
import re
import os

file = sys.argv[1]#输入文件名
file1 = sys.argv[2]#输出文件名
image_suffix=["png","jpg","jpeg","tiff","gif","psd","raw","eps","svg","pdf","bmp"]

# 删除所有不在md中的图片
def delete_images(path=r"./_v_images/"):
    images = os.listdir(path)
    for i in images:
        exist = False
        for j in r1:
            if i == j:
                exist = True
                break
        if exist == False:
            #print(i)
            os.remove(path+i)

# 读取md文件内容
try:
    f = open(file,'r+',encoding = 'utf-8')
except IOError as e:
    print("error:",e)
    f.close()
str = f.read()
f.close()
# 找到所有的图片文件名
r1 = []
for s in image_suffix:
    r1 += re.findall(r"\d*_\d*."+s,str)
# 替换图片文件名为typora可识别
r2 = str
for s in image_suffix:
    r2 = re.sub("."+s+r" =\d*x","."+s,r2)
f1 = open(file1,"w+")
f1.write(r2)
f1.close()

# 确认是否删除多余的图片文件
path = r"./_v_images/"
images = os.listdir(path)
print(file+"  中引用",len(r1),"个图片")
print(path+"  中共有",len(images),"个文件")
print("是否删除多余图片文件？（Y/N）")
a = input()
if a == "Y" or a == "y":
    delete_images(path)
    print("\n删除多余图片文件成功")
    print(file+"  中引用",len(r1),"个图片")
    images = os.listdir(path)
    print(path+"  中共有",len(images),"个文件")
else:
    print("取消删除文件操作")
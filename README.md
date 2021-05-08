# 解决vnote图片无法为typora所识别的问题

## overview

我习惯用vnote写项目文档

但是有的时候需要提交项目文档和代码

大家习惯用typora查看图片

Q1：而如果在vnote中修改了图片大小，则其图片格式不支持typora查看

Q2：vnote是把所有的图片放到一个文件夹下，而我不希望我的其它md文件的图片也发送过去

因此通过这个代码可以解决

1. vnote图片无法被typora识别问题
2. 删除_v_images中没有被本md引用的多余的图片

## usage

python main.py *file_name* *output_name*

修改源md文件到ouput文件中，中间会询问是否需要删除多余的图片文件

默认图片目录为./_v_images/


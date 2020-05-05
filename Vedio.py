# -*- coding = utf-8 -*-

import cv2
import os
import numpy

import time

from PIL import Image

gray_num = list("$@B%8&WM*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def main():
    # video(input())
    # saveVideo(path=input("请输入要读取的视频地址："), savepath=input("请输入要保存的地址："))
    # picvideo(input(), (512, 384))
    img_to_char(35)


def video(videoPath : str):
    cap = cv2.VideoCapture(videoPath)  # 读取视频

    while True:
        success, frame = cap.read()  # 读取帧
        if not success:
            break
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        tsize = os.get_terminal_size()
        # fixFrame = cv2.resize(grayFrame, (tsize.columns, tsize.lines))
        fixFrame = cv2.resize(grayFrame, (tsize.columns, tsize.lines))
        img_array = numpy.array(fixFrame, "f")
        ascillFrame = ""
        for line in img_array:
            for p in line:
                # p 浮点数数字
                n = (p/255)*(len(gray_num)-1)  # 灰度像素点在字符列表的位置
                index = int(n)  # 化为整数
                ascillFrame += gray_num[index]
            ascillFrame+="\n"
        print(ascillFrame)
        os.system('cls')
    cap.release()  # 关闭视频

################################################################################################
# 读取帧保存
def saveVideo(path, savepath):
    # D:\projects\Python\a\badapple.mp4
    # D:\projects\Python\Vedio\badapple
    cap = cv2.VideoCapture(path)
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver) < 3:
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    i = 1
    while True:
        success, frame = cap.read()
        if not success:
            break
        cv2.imwrite(savepath + "\\" + str(i).zfill(4) + '.png', frame)  # 存储为图像
        i += 1
        # print(i, "帧解析完成")
    print("解析完成")

# 读取帧合成视频
def picvideo(path, size, fps = 30):
    # path = D:\projects\Python\Vedio\badapple
    filelist = os.listdir(path)  # 获取该目录下的所有文件名

    file_path = path + ".mp4"  # 导出路径
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）
    video = cv2.VideoWriter(file_path, fourcc, fps, size)
    for item in filelist:
        if item.endswith('.png'):   # 判断图片后缀是否是.png
            item = path + '/' + item
            img = cv2.imread(item)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
            video.write(img)        # 把图片写进视频
            print(item + "写入成功！")
    video.release()  # 释放
    print("合成完成")

def img_to_char(height):
    '''
    将图片转化为字符
    height是字符串图片的高度
    '''

    # 读取图片
    img = Image.open(r"D:\projects\Python\Vedio\badapple\0191.png")
    # img = Image.open(r"D:\projects\Python\a\images\10.png")
    img_width, img_height = img.size
    # 设置大小
    width = int(3 * height * (img_width / img_height))
    img = img.resize((width, height), Image.ANTIALIAS)
    # 读取图片的灰度值矩阵
    data = numpy.array(img.convert('L'))
    # 设定字符,字符数要是256的因子，这里取32
    chars = "#RMNHQODBWGPZ*@$C&98?32I1>!:-;. "
    N = len(chars)
    # 计算每个字符的区间,//取整
    n = 256 // N
    # result是字符结果
    result = ''
    for i in range(height):
        for j in range(width):
            result += chars[data[i][j] // n]
        result += '\n'
    with open('img.txt', mode='w') as f:
        f.write(result)

def txt_read(path):
    # D:\projects\Python\Vedio\img.txt
    with open(path) as t:
        a = t.read()
    print(a)


if __name__ == "__main__":
    # main()
    txt_read(r"D:\projects\Python\Vedio\img.txt")

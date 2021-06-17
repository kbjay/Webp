import os

resSet = []


# 获取xxxdpi的资源数组
def createResSet(xxxPath):
    for root, dirs, files in os.walk(xxxPath):
        for file in files:
            resSet.append(file)


# 遍历xdpi,重复就删除
def removeDuplicateRes(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file in resSet:
                os.remove(os.path.join(root, file))


if __name__ == "__main__":
    createResSet("D:\project\global-onejoy-android\\app\src\main\\res\mipmap-xxxhdpi")
    removeDuplicateRes("D:\project\global-onejoy-android\\app\src\main\\res\mipmap-xxhdpi")
    removeDuplicateRes("D:\project\global-onejoy-android\\app\src\main\\res\mipmap-xhdpi")
    removeDuplicateRes("D:\project\global-onejoy-android\\app\src\main\\res\mipmap-hdpi")
    removeDuplicateRes("D:\project\global-onejoy-android\\app\src\main\\res\mipmap-mhdpi")

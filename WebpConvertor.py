import os


# 扫描指定目录下的png跟jpg图片转成webp
def convert(exePath, path):
    for item in os.listdir(path):

        sourcePath = path + "/" + item

        # 如果是文件夹，递归
        if os.path.isdir(sourcePath):
            convert(exePath, sourcePath)
            continue

        # 如果不是文件，那么继续
        if not os.path.isfile(sourcePath):
            continue

        if item.endswith(".9.png"):
            continue

        if item.endswith(".9.jpg"):
            continue

        # 如果不是jpg跟png结尾的，那么继续
        if not os.path.splitext(sourcePath)[1] in ['.png', '.jpg']:
            continue

        print("开始转换->" + sourcePath)

        # 执行转换命令
        webpPath = os.path.splitext(sourcePath)[0] + ".webp"
        commond = exePath + " -q 80 " + sourcePath + " -o " + webpPath
        os.system(commond)

        # 删除原图跟webp中大的那个
        sourceSize = os.path.getsize(sourcePath)
        webpSize = os.path.getsize(webpPath)
        if sourceSize >= webpSize:
            os.remove(sourcePath)
        else:
            os.remove(webpPath)

        print("转换结束->", sourceSize, webpSize)


def convertArray(exePath, paths):
    for path in paths:
        convert(exePath, path)


if __name__ == '__main__':
    # cwebp.exe 目录，需要下载官方web转换工具
    encoder_path = "D:/libwebp-1.0.2-windows-x64/bin/cwebp.exe"
    # 需要转化的文件夹目录
    rootPaths = [
        # "D:/HW/XiaoiceAICProjs/private/huawei/client/Xiaoice.Joypark/xiaoicesdk.joypark.book/src",
        # "D:/HW/XiaoiceAICProjs/private/huawei/client/Xiaoice.Joypark/xiaoicesdk.joypark.paint/src",
        # "D:/HW/XiaoiceAICProjs/private/huawei/client/Xiaoice.Joypark/xiaoicesdk.joypark.dialog/src",
        # "D:/HW/XiaoiceAICProjs/private/huawei/client/Xiaoice.Joypark/xiaoicesdk.joypark.portal/src",
        "C:/Users/v-zewan/Desktop/小兵 - 副本"]

    convertArray(encoder_path, rootPaths)

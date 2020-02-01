# coding:utf8
import os


def rename():
    path = "D:\\work\\nzpt\\new\\1"
    file_list = os.listdir(path)
    for files in file_list:
        print("原来文件名字是是：", files)
        old_name = os.path.join(path, files)
        if os.path.isdir(old_name):
            continue
        file_name = os.path.splitext(files)[0]
        file_type = os.path.splitext(files)[1]
        print(file_name, ":", file_type)
        if file_type == ".jfif":
            file_type_new = ".jpg"
            new_dir = os.path.join(path, file_name+file_type_new)
            print("新文件目录为", new_dir)


if __name__ == '__main__':
    rename()
    print("重命名结束")

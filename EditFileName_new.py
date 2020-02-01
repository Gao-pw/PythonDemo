# coding:utf8
# 添加文件夹递归
import os
i = 0


def find_path(dir_path):
    global i
    file_list = os.listdir(dir_path)
    for files in file_list:
        i += 1
        print("原来文件名字是是：", files, "第", i, "个")
        old_dir = os.path.join(dir_path, files)
        if os.path.isdir(old_dir):
            find_path(old_dir)
        rename(files, dir_path, old_dir)


def rename(file, dir_path, old_dir):
    file_name = os.path.splitext(file)[0]
    file_type = os.path.splitext(file)[1]
    if file_type == ".jfif":  # 原来格式
        file_type_new = ".jpg"  # 现有格式
        new_dir = os.path.join(dir_path, file_name + file_type_new)
        print("新文件目录为", new_dir)
        os.rename(old_dir, new_dir)


if __name__ == '__main__':
    path = "D:\\work\\nzpt\\new\\1"  # 根目录
    find_path(path)
    print("重命名结束，共计", i, "个文件")

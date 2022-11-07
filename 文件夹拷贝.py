#拷贝
import os
import shutil
import time
import datetime

list = ['20211121','20211219','20220102','20220116']
f  = []
for i in list:
    a=datetime.datetime.strptime(i,'%Y%m%d')
    f.append(a)
# t1 = time.strftime("%Y%m%d", time.localtime())
# t1 = time.strftime("%Y%m%d", time.localtime())
t1t = datetime.datetime.strptime('20220109','%Y%m%d')

diff = (t1t - f[0]).days
if diff % 14 ==0:

    t1t = t1t.date()
    source_path = os.path.abspath(r'D:\数据分析\桌面')
    target_path = os.path.abspath(r'D:\数据分析\%s'%t1t)
    if not os.path.exists(target_path):
        # 如果目标路径不存在原文件夹的话就创建
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(target_path)
        shutil.copytree(source_path, target_path)
    print('copy dir finished!')
else :
    t2 = (f[0]+ datetime.timedelta(days=int(diff/14)*14)).date()
    source_path = os.path.abspath(r'D:\数据分析\桌面')
    target_path = os.path.abspath(r'D:\数据分析\%s'%t2)
    if not os.path.exists(target_path):
        # 如果目标路径不存在原文件夹的话就创建
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(target_path)
        shutil.copytree(source_path, target_path)
    print('copy dir finished!')

#以下为复制所有文件
# if not os.path.exists(target_path):
#     os.makedirs(target_path)

# if os.path.exists(source_path):
#     # root 所指的是当前正在遍历的这个文件夹的本身的地址
#     # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
#     # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
#     for root, dirs, files in os.walk(source_path):
#         for file in files:
#             src_file = os.path.join(root, file)
#             shutil.copy(src_file, target_path)
#             print(src_file)
#
# print('copy files finished!')




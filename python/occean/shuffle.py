import codecs
import random
lines = []
# 防止乱码，用codecs模块打开中文文件
with codecs.open("./7-29-156.txt", 'r', 'utf-8') as infile:
    # 将每行数据依次加入数组
    for line in infile:
        lines.append(line)
# 数组乱序
random.shuffle(lines)
# 乱序后文件写入新文件
with codecs.open("./luanxu.txt", 'w', 'utf-8') as f:
    for line in lines:
        f.write(line)

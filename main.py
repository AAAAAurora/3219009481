# encoding=utf-8
import math
import re
import jieba
import sys


# 从绝对路径里读取文本信息，并返回文本信息
def rfile(filepath):
    file = open(filepath, 'r', encoding='utf-8') # 打开文本
    message = file.read() # 读取文本
    file.close() # 关闭文本
    return message # 返回文本信息


# 分词：中文按词语分割，英文按单词分割，数字按空格分割，其中去掉标点符号
def cut(message):
    # 去掉标点符号，如“，”、“。”、“、”、“；”等等
    comp = re.compile('[^A-Z^a-z0-9\u4e00-\u9fa5]')
    words = jieba.lcut(comp.sub('', message), cut_all=False)
    # 去掉空格
    word = [w for w in words if len(w.strip()) > 0]
    return word # 返回切割好的单词列表


# 对单词列表里各词语出现次数进行统计
def count(list_orig, list_else):
    # 将两个单词列表的单词进行合并
    keyword = list(set(list_orig + list_else))
    # 遍历keyword和list_orig，统计第一个句子各单词的词频
    vec1 = []
    for i in range(len(keyword)): # 遍历keyword
        vec1.append(0)
        for j in range(len(list_orig)): # 遍历list_orig
            if keyword[i] == list_orig[j]: #如果keyword和list_orig出现一样的词语，则+1
                vec1[i] += 1
                continue

    # 遍历keyword和list_else，统计第一个句子各单词的词频
    vec2 = []
    for k in range(len(keyword)): # 遍历keyword
        vec2.append(0)
        for m in range(len(list_else)): # 遍历list_else
            if keyword[k] == list_else[m]: # 如果keyword和list_orig出现一样的词语，则+1
                vec2[k] += 1
                continue
    return vec1, vec2 # 返回频数向量列表


# 计算两篇文本的余弦相似度
def CosSimilarity(vec_orig, vec_else, dim=256):
    # 初始化
    vec_orig_orig = 0.0
    vec_else_else = 0.0
    vec_orig_else = 0.0
    for i in range(dim):
        vec_orig_orig += vec_orig[i] * vec_orig[i]
        vec_else_else += vec_else[i] * vec_else[i]
        vec_orig_else += vec_orig[i] * vec_else[i]
    vec_orig_orig_sqrt = vec_orig_orig ** 0.5
    vec_else_else_sqrt = vec_else_else ** 0.5
    try:  # 正常执行
        cos = vec_orig_else/(vec_orig_orig_sqrt*vec_else_else_sqrt)*0.5+0.5 # 计算余弦相似度
        return cos
    except ZeroDivisionError: #输入了空白的文本，此时除数为0，报错
        print('Sorry, the text is blank.')
        return 0


def main_test(path_orig, path_else, save_path):
    #绝对路径：
    #path_orig:
    # L:\pythonProject5\text\orig.txt
    #path_else:
    #L:\pythonProject5\text\orig_0.8_add.txt
    #L:\pythonProject5\text\orig_0.8_del.txt
    #L:\pythonProject5\text\orig_0.8_dis_1.txt
    #L:\pythonProject5\text\orig_0.8_dis_10.txt
    #L:\pythonProject5\text\orig_0.8_dis_15.txt
    #save_path:
    # L:\pythonProject5\text\result.txt

    try:
        # 计算
        file_orig = rfile(path_orig) # 读取原文本
        file_else = rfile(path_else) # 读取抄袭文本
        cut_orig = cut(file_orig) # 对原文本进行切割
        cut_else = cut(file_else) # 对抄袭本进行切割
        list_orig, list_else = count(cut_orig, cut_else)# 对原文本和抄袭文本进行分词
        result = CosSimilarity(list_orig, list_else) # 计算余弦相似度

        # 输出

        print("The article being compared is"+str(path_orig) + "\t"+"and"+ "\t" + str(path_else))
        print("The similarity between the two articles is"+" %.2f%%\n" % (result * 100))
        # 将结果写如result.txt文本中
        file_result = open(result_save_path, 'a', encoding="utf-8")
        file_result.write("The similarity between the two articles is"+" %.2f%%" % (result * 100)+"("+str(path_orig) + "\t"+"and"+ "\t" + str(path_else)+")")
        file_result.write("\n\n")
        file_result.close()
    # 输入文件路径有误
    except FileNotFoundError:
        print("Sorry, the text does not exist.")


if __name__ == '__main__':
    filepath_orig = ''
    filepath_else = ''
    result_save_path = ''
    try:#正常运行
        # 与命令行参数交互
        filepath_orig = sys.argv[1]
        filepath_else = sys.argv[2]
        result_save_path = sys.argv[3]
    except IndexError:
        filepath_orig = input("Please enter the original text path:")
        filepath_else = input("Please enter the copied text path:")
        result_save_path = input("Enter the path to the text you want to save the similarity result：")

    main_test(filepath_orig, filepath_else, result_save_path)
    input()

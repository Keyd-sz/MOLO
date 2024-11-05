# # # # # # str="青青子衿，悠悠我心，但惟君故，沉吟至今"
# # # # # # newStr1 = str.replace("，", '\n')
# # # # # # print(newStr1)
# # # # # #
# # # # # # newStr2 = str.replace("，", "\n", 2)
# # # # # # print(newStr2)
# # # # #
# # # # # filepath = '../DB/train_positive.txt'
# # # # # _comments = open(filepath, encoding='utf-8-sig').read().replace('\n', '')
# # # # # print(_comments)
# # # # str = "Line1-sztu \nLine2-sz \nLine3-szt"
# # # # print(str.split( ))
# # # # print(str.split(' ', 1))
# # #
# # #
# # # # txt = "SZTU#Big#Data#Internet"
# # # # # print(txt.split('#'))
# # # # x = txt.split('#',1)
# # # # print(x)
# # #
# # # filepath = "../DB/train_positive.txt"
# # # _comment = open(filepath,encoding='utf-8-sig').read().replace('\n', '').split('</review>')
# # # print(_comment)
# #
# # names = ['sztu', 'big', 'data', 'ai', 'computer',
# #          'science', 'internet']
# # names.remove('data')
# # print(names)
# # names.remove('internet')
# # print(names)
#
# filepath = "../DB/train_positive.txt"
# _comments = open(filepath,encoding='utf-8-sig').read().replace('\n', '').split('</review>')
# while '' in _comments:
#     _comments.remove('')
# print(_comments)
# str1 = "this is string example....wow!!!"
# str2 = "exam"
# print(str1.find(str2))
# print(str1.find(str2, 10))
# print(str1.find(str2, 40))

# info = 'abca'
# print(info.find('a'))
# print(info.find('a',1))
# print(info.find('3'))

# filepath = '../DB/train_positive.txt'
# print(filepath.find('pos'))
# print(filepath.find('pos') > 0)

import re
# pattern = re.compile(r'\d+')
# m = pattern.match('one12twothree34four')
# print(m)
# m = pattern.match('one12twothree34four', 2, 10)
# print(m)
# m = pattern.match('one12twothree34four', 3, 10)
# print(m)
# print(re.match('www', 'www.sztu.edu.cn').span())
# print(re.match('edu', 'www.sztu.edu.cn'))
#
# line = "Cats are smarter than rabbits"
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")

# name = ['Big', 'Data', 'Internet']
# name.append('SZTU')
# print("Updated list: ", name)
# pattern = re.compile(r'\d+')
# result1 = pattern.findall('sztu 123 rontgen 456')
# result2 = pattern.findall('sz88tu123rontgen456', 0, 17)
# print(result1)
# print(result2)
# filepath = '../DB/train_positive.txt'
# _comment = open(filepath,encoding='utf-8-sig').read().replace('\n', '').split('</review>')
# while '' in _comment:
#     _comment.remove('')
# local_comments = []
#
# if filepath.find('pos') > 0:
#     pattern = re.compile('^.*>(.*)')
#     text = pattern.findall(_comment[0])
#     local_comments.append(text[0])
#     text = pattern.findall(_comment[1])
#     local_comments.append(text[0])
# print(local_comments)
#
# train_comment = re.sub('\d', ' NUM ', '对孩子很有帮助。印刷质量也很好。但是：1、文字错误的地方很多 2.CD制作很粗糙。')
# print(train_comment)
# train_comment = re.sub('\d', ' NUM ', 'TB上只要330， 要是这里降到350我肯定买，毕竟在JOYO买了很多东西，信得过。')
# print(train_comment)

import jieba
seg_list = jieba.cut("他被伦琴人工智能实验班录取了", cut_all=True)
print(" [全模式] : " + "/ ".join(seg_list))
seg_list = jieba.cut("他被伦琴人工智能实验班录取了", cut_all=False)
print(" [精细模式] : " + "/ ".join(seg_list))




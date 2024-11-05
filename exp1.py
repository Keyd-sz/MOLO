# import re
# import jieba
# from sklearn.feature_extraction.text import TfidfVectorizer
# def clean_symbols(text):
#     text = re.sub('[!！]+', "!", text)
#     text = re.sub('[?？]+', "?", text)
#     text = re.sub("[a-zA-Z#$%&\'()*+,-./:;：<=>@，。*、...【】《》""''[\\]^_`{|}~]+", "00v", text)
#     return re.sub("\s+", " ", text)
#
# comment1 = '太好听了.德国造的.不买很可惜.我已经买了,不在JOYO,只要118元'
# comment2 = '包装盒破裂，拆开了才发现！'
# comment3 = '很好！35元绝对超值。内容好，又很有趣，而且是中文配音的，很适合儿童。'
# print(comment1+'\n'+comment2+'\n'+comment3)
# print('-------------------------------------------------')
#
# comment1 = clean_symbols(comment1)
# comment2 = clean_symbols(comment2)
# comment3 = clean_symbols(comment3)
# print(comment1+'\n'+comment2+'\n'+comment3)
# print('-------------------------------------------------')
#
# comment1 = re.sub('\d', ' NUM ', comment1)
# comment2 = re.sub('\d', ' NUM ', comment2)
# comment3 = re.sub('\d', ' NUM ', comment3)
# print(comment1+'\n'+comment2+'\n'+comment3)
# print('-------------------------------------------------')
#
# cut1 = jieba.cut(comment1)
# cut2 = jieba.cut(comment2)
# cut3 = jieba.cut(comment3)
#
# seg = [word for word in cut1]
# comment1 = " ".join(seg)
# seg = [word for word in cut2]
# comment2 = " ".join(seg)
# seg = [word for word in cut3]
# comment3 = " ".join(seg)
# print(comment1+'\n'+comment2+'\n'+comment3)
# print('-------------------------------------------------')
#
# corpus = [comment1, comment2, comment3]
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(corpus)
# print(vectorizer.get_feature_names_out())
# print(X.shape)
# print(X)
#

from sklearn.metrics import classification_report
y_true = [1, 2, 8, 8, 8]
y_pred = [1, 1, 8, 8, 2]
target_names = ['class0', 'class1', 'class2']
print(classification_report(y_true, y_pred, target_names=target_names))
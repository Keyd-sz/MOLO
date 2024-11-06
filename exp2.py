import jieba
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

def clean_symbols(text):
    text = re.sub('[!！]+', "!", text)
    text = re.sub('[？?]+', "?", text)
    text = re.sub("[a-zA-Z#$%&\'()*+,-./:;：<=>@，。*、…【】《》\"\'[\\]^_`{|}~]+", " 00V ", text)
    return re.sub("\s+", " ", text).strip()

# 读取训练集评论
with open('../DB/train_positive.txt', 'r', encoding='utf-8') as f:
    train_positive = f.read().splitlines()
with open('../DB/train_negative.txt', 'r', encoding='utf-8') as f:
    train_negative = f.read().splitlines()

# 读取测试集评论
with open('../DB/test_combined.txt', 'r', encoding='utf-8') as f:
    test_comments = f.read().splitlines()

# 读取停用词
stopword_pth = "../DB/stopwords.txt"
with open(stopword_pth, 'r', encoding='utf-8') as f:
    stopword = f.read().splitlines()

# 处理训练集评论
train_comments = train_positive + train_negative
train_comment_cleaned = []

for train_comment in train_comments:
    # 1. 调用 clean_symbols 处理 train_comment 的特殊符号
    train_comment = clean_symbols(train_comment)
    # 2. 调用 re.sub 将 train_comment 数字换成特殊符号 ' NUM '
    train_comment = re.sub('[1234567890]+', ' NUM ', train_comment)
    # 3. jieba.cut 对 train_comment 进行分词
    cut_train = jieba.cut(train_comment)
    # 4. 去除停用词
    seg_train = [word for word in cut_train if word not in stopword]
    # 5. 重新组合成字符串
    train_comment_cleaned.append(" ".join(seg_train))

# 处理测试集评论
test_comment_cleaned = []
y_test = []
for line in test_comments:
    line = line.strip()
    # 检查是否是包含 label 的行
    if line.startswith('<review'):
        # print("Get it: "+line)
        # 提取标签信息
        label_match = re.search(r'label="(\d)"', line)
        if label_match:
            label = int(label_match.group(1))
            y_test.append(label)
            # print("Get label: "+str(label))
    elif line and 'review' not in line:
        # 处理评论内容
        test_comment = line
        test_comment = clean_symbols(test_comment)
        test_comment = re.sub('[1234567890]+', ' NUM ', test_comment)
        cut_test = jieba.cut(test_comment)
        seg_test = [word for word in cut_test if word not in stopword]
        # 将清洗后的评论文本加入到 test_comment_cleaned 列表中
        test_comment_cleaned.append(" ".join(seg_test))

# 打印前5条处理后的评论
for i in range(0, 5):
    print(train_comment_cleaned[i])
print("-----------------------------")
for i in range(0, 5):
    print(test_comment_cleaned[i])

# 准备标签
y_train = [1] * len(train_positive) + [0] * len(train_negative)

# 特征提取
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_comment_cleaned)
X_test = vectorizer.transform(test_comment_cleaned)

# 数据分割
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# 打印特征矩阵和标签的形状
print("X_train shape:", X_train.shape)
print("y_train shape:", len(y_train))
print("X_test shape:", X_test.shape)
print("y_test shape:", len(y_test))
# print(X_test)
# print(y_test)

# 1
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')

para_c = np.logspace(-5, 2, 15)
model = GridSearchCV(estimator= LogisticRegression(penalty='l2'), param_grid={'C':para_c}, scoring='f1', cv=10)
model.fit(X_train, y_train)
prediction = model.predict(X_test)
print("Report of LogisticRegression")
print(classification_report(y_test, prediction))


# 2
from sklearn.naive_bayes import MultinomialNB
params_alpha = [1]
model = GridSearchCV(estimator=MultinomialNB(fit_prior=True), param_grid = {'alpha':params_alpha}, scoring='f1', cv=10)
model.fit(X_train, y_train)
predic = model.predict(X_test)
print("Report of NaiveBayes")
print(classification_report(y_test, predic))

# 3
from sklearn import svm
params = [{'kernel':['linear'], 'C':[1, 10]},{'kernel':['poly'], 'C':[1]}, {'kernel':['rbf'], 'C':[10], 'gamma':[1, 0.1]}]
model = GridSearchCV(estimator=svm.SVC(), param_grid=params, scoring='f1', cv=10)
model.fit(X_train,y_train)
prediction = model.predict(X_test)
print("Report of SVM")
print(classification_report(y_test, prediction))

# 15:14
print("This is my change,11111")

print("This is Student2 change, 2222")

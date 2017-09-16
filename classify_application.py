import pandas as pda
import numpy as npy
#1，使用下载数据导入的方法
filename="下载的数据"
dataf=pda.read_csv(filename)
x=dataf.iloc[:,0:4].as_matrix()
# iloc[:,0:4] 表示取所有行的0-4列，也就是特征值
y=dataf.iloc[:,4,5].as_matrix()
# 分类结果(把文字转换成数字)

#2，sklearn中的数据集
from sklearn import datasets
x=irisdata.data#特征值
y=irisdata.target#训练结果

#把所有数据分成历史数据和训练数据两部分：
from sklearn.model_selection import train_test_split(x,y,test_size=0.5,random_state=20)
#test_size分割训练数据和历史数据，0.5表示测试数据的比例为0.5

#1.1，使用自己写的KNN算法进行分类
#把knn算法贴在这里
#调用如下：
for i in range(0,len(x_test.tolist()))
#用tolist()把x_test转换成list，把每一个x_test都放进算法里进行计算
	predict=knn(3,x_test.tolist()[i],x_train,y_train.tolist())
	y2.append(predict)#把结果添加到y2中
#把结果进行对比
y2==y_test#得到一个true/false 列表 可以看准确率

#1.2，使用sklearn中knn实现
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
model.fit(x_train,y_train)#训练数据
y2=model.predict(x_test)#训练结果

#2.1，使用自己写的bayes算法实现
#把knn算法复制过来
bys=Bayes()
bys.fit(x_train.tolist(),y_train.tolist())
#训练数据都转换成列表格式
labels=[0,1,2]
y2=[]
for i in range(0,len(x_test.tolist())):
	predict=bys.btest(x_test.tolist()[i],labels)
	#把每一个测试集，和所有可能的label调用进来做测试
	y2.append(predict)
#2.2，集成bayes
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(x_train,y_train)
expected = y_test
predicted=model.predict(x_test)
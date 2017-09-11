#! -*- coding: utf-8 -*-
import numpy as npy
import numpy
from numpy import *
import operator
from os import lisdir

class Bayes:
	def __init__(self):
	#用来完成初始化
		self.length=-1
		self.labelcount=dict()
		#每个类别的概率，以字典方式存储
		#{"classA"：P(A),"classB":P(B) ...}
		self.vectorcount=dict()
		#以字典的方式存储每个类别，以及他们的特征向量
		#{"classA":[特征向量1,特征向量2,...],...,"classN":[特征向量1,特征向量2,...]}
	def fit(self,dataSet:list,label:list):
	#训练数据
		if(len(dataSet)!=len(labels)):
			raise ValueError("输入的训练数组跟训练数组长度不一致")
		self.length=len(dataSet[0])#训练数据特征值的长度
		'''
			>>> dataset=([0,2],[2,1],[0,0])
			>>> len(dataset)
			3
			>>> len(dataset[0])
			2
		'''
		labelsnum=len(labels)#历史中的类别数量
		norlabels=set(labels)#不重复类别
		'''
			>>> label=('c1','c0','c1')
			>>> len(label)
			3
			>>> set(label)
			{'c0', 'c1'}
		'''
		for item in norlabels:
			thislabel=item
			self.labelcount[thislabel]=labels.count(thislabel)/labelsnum
			#labels.count(c0):labels中'c0'的数量/labelsum(总数)
			#求P(c),每种类别占总数的比例
		#通过zip将两个数组交叉存放
		'''
		x1=[a,b,c]
		x2=[e,f,g]
		k=zip(x1,x2)
		k:[(a,e),(b,f),(c,g)]
		'''
		for vector,label in zip(dataSet,labels):
			if (label not in self.vectorcount):
				self.vectorcount[label]=[]
			self.vectorcount[label].append(vector)#储存在dict当中，label为key
		print("训练结束")
		return self
		#训练过程就是把数据整理成可以统计概率的形式
	def btest(self,TestData,labelsSet):
		if(self.length==-1)
			raise ValueError("你还没有训练，请先训练")
		#计算testdata分别为各个类别的概率
		lbDict=dict()#{"类别1"：概率1，"类别2"：概率2}
		for thislb in labelsSet:
			p=1
			alllabel=self.labelcount[thislb]#当前类别的概率跑P(c)
			allvector=self.vectorcount[thislb]#当前类别的所有特征向量
			vnum=len(allvector)#当前类别特征向量个数
			allvector=numpy.array(allvector)#转置一下
			'''
			把：[[t1,t2,t3,t4],[t1,t2,t3,t4]]
			转制成：[t1,t1],[t2,t2],[t3,t3]
			'''
			for index in range(0,len(TestData))#依次计算各特征的概率
				vector=list(allvector[index])
				p*=vector.count(TestData[index])/vnum#p(当前特征|C)
				#如testdata[0]:0,vector:[1,0,1,0,0,1,1],p为3/7
			lbDict[thislb]=p*alllabel#alllabel相当于p(c)
		thislabel=sorted(lbDict,key=lambda x:lbDict[x],reverse=True)[0]
		return thislabel



		#调用模块实现：
		from sklearn.naive_bayes import GaussianNB
		model = GaussianNB()#建立模型
		model.fit(x,y)#训练
		expected = y
		predicted = model.predict(x)

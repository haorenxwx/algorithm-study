from numpy import *
import operator

def KNN(k,test_data,train_data,labels):
	#k:取前多少个进行统计
	#labels：与train_data一一对应的一维列表
	traindatasize=train_data.shape[0]
	#计算train_data的维度（即有多少组traindata）
	dif=tile(test_data,(traindatasize,1))-train_data
	#把testdata和traindata划为同一个维度进行计算
	'''
	tile的用法：
	>>> from numpy import *
	>>> x=numpy.array([1,2,3,4])
	>>> y=[1,2,3,4]
	>>> xtile=tile(x,(5,1))
	>>> ytile=tile(y,(5,1))
	>>> xtile
	array([[1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4]])
	>>> ytile
	array([[1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4]])
	>>> xtile=tile(x,(5,2))
	>>> xtile
	array([[1, 2, 3, 4, 1, 2, 3, 4],
       [1, 2, 3, 4, 1, 2, 3, 4],
       [1, 2, 3, 4, 1, 2, 3, 4],
       [1, 2, 3, 4, 1, 2, 3, 4],
       [1, 2, 3, 4, 1, 2, 3, 4]])
	>>>
	'''
	sqdif=dif**2
	sumsqdif=sqdif.sum(axis=1)
	#axis表示横向相加，变成1维
	distance=sumsqdif**0.5
	#计算每组数据的欧拉距离（一维数组）
	sortdistance=distance.argsort()
	#把得到的欧拉距离按从远到近排序
	'''
	argsort的功能
	按照数字从大到小排序并取出下标放在列表中
	>>> x=numpy.array([5,3,6,1,2])
	>>> y=[5,3,6,1,2]
	>>> x1=x.argsort()
	>>> x1
	array([3, 4, 1, 0, 2], dtype=int64)
	>>> y1=y.argsort()
	AttributeError: 'list' object has no attribute 'argsort'

	list不能sort或者argsort
	'''
	count={}
	#count为一个字典列表
	for i in range(0,k):
		vote=labels[sortdistance[i]]
		count[vote]=count.get(vote,0)+1
		#给字典count赋值，key是vote(代表testdata所对应的label)
		#get()用力来获取字典的值
		'''
		dict数据类型中get的用法：
		>>> count={1:2,3:4}
		>>> vote=4
		>>> count.get(vote,0)
		0
		如果vote的值没有出现在dict的key中，返回vote，后的值
		>>> count.get(vote,'nouse')
		'nouse'
		'''
	sortcount=sorted(count.item(),key=operator.itemgetter(1),reverse=True)
	#operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序数
	'''
	>>> a=[1,2,3]
	>>> b=operator.itemgetter(1)
	>>> b(a)
	2
	'''
	#上面sorted函数中
	#key=operator.itemgetter(1)
	#只取label
	#reverse=True，表示从大到小排列
	return sortcount[0][0]
	#返回第一个值，数量最多

	#knn算法还可以用sklearn模块实现
	from sklearn.neighbors import KNeighborsClassifier
	model=KNeighborsClassifier()
	model.fit(x,y)
	#x是历史数组特征，(相当于前面算法中的data_train)
	#y是历史数据的结果(相当于前面算法中的data_label)
	y2=model.predict(x2)
	#X2是测试特征(test_data)
	#y2是测试数据的结果



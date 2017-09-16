#决策树算法实现
import pandas as pandas
fname="datafile.csv"#以csv数据类型举例
dataf=pda.read_csv(fname,encoding="gbk")
x=dataf.iloc[:,1:5].as_matrix()
y=dataf.iloc[:,5].as_matrix()
for i in range(0,len(x)):
	for j in range(0,len(x[i])):
		thisdata=x[i][j]
		if (thisdata=="是" or thisdata=="多" or thisdata="高"):
			x[i][j]=int(1)
		else:
			x[i][j]=int(-1)
for i in range(0,lem(y)):
	thisdata=y[i]
	if(thisdata=="高"):
		y[i]=1
	else:
		y[i]=-1
xf=pda.DataFrame(x)#转成数据框
yf=pda.DataFrame(y)
x2=xf.as_matrix().astype(int)#转化为int数据类型
y2=yf.as_matrix().astype(int)#转化为int数据类型
from sklearn.tree import DecisionTreeClassifier as DecisionTreeClassifier
dtc=DTC(criterion="entropy")#用信息熵完成决策树
dtc.fit(x2,y2)
print(dtc.predict(x2))
#打印结果


#可视化决策树
#需要安装graphviz.msi 配置环境变量后可以使用
from sklearn.tree import export_graphviz
from sklearn.external.six import StringIO
with open("tree.dot","w") as file:#把file放到tree.dot
	file=export_graphviz(dtc,feature_name=["shizhan","keshishu","cuxiao","ziliao"],out_file=file)
#graphviz 把生成的.dot转化成png格式，可以看到完整的决策树（可以看到优先考虑哪个特征）





# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:24:29 2020

@author: ASUS
"""
#練習01
import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

height  =np.array([147.9,163.5,159.8,155.1,163.3,158.7,172.0,161.2,153.9,161.6])
weight = np.array([41.7,60.2,47.0,53.2,48.3,55.2,58.5,49.0,46.7,52.5])

x = pd.DataFrame(height,columns = ['height'])
y = pd.DataFrame(weight,columns = ['weight'])

lm = LinearRegression()
lm.fit(x,y)

print('回歸係數：',lm.coef_)
print('截距：',lm.intercept_)

new_height = pd.DataFrame(np.array([155,165,180]))
predicted_weight=lm.predict(new_height)
print(predicted_weight)
plt.scatter(height,weight)
regerssion_weight=lm.predict(x)
plt.plot(height,regerssion_weight,color="b")
plt.plot(new_height,predicted_weight,color="r",marker="o",markersize=10)
plt.show()

-----------------------------------------
練習02
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()

X = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns = ["MEDV"])
y = target["MEDV"]

lm = LinearRegression()
lm.fit(X, y)
regression_d = lm.predict(X)

X1 = X.drop(columns=['s1','s2','s3','s4','s5','s6'])
lm.fit(X1, y)
regression_d1 = lm.predict(X1)

plt.scatter(y, regression_d)
plt.show()

plt.scatter(y, regression_d1)
plt.show()

--------------------------------------------------------------
練習03

#殘差值 練習03
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

diabetes =datasets.load_diabetes()#糖尿病病患資料集
#age年齡 sex性別 bmi()體質指數 bp平均血壓 
#s1~s6 一年後疾病級數指標 target 一年後患病定量指標
x =pd.DataFrame(diabetes.data ,columns =['age', 'sex', 'bmi', 'bp', 
                                         's1','s2','s3','s4','s5','s6'])
#col =diabetes.feature_names
target =pd.DataFrame(diabetes.target, columns =['target'])
y =target['target']

lm =LinearRegression()
lm.fit(x,y)
# print('迴歸係數',lm.coef_)
# print('截距',lm.intercept_) #都會變動
#預測 
new_s =lm.predict(x)
#01
mse =np.mean((y-new_s)**2)
print('--不分割資料集--')
print('不分割資料集,MSE:',mse)
print('不分割資料集,R-squared:',lm.score(x,y))

#02 3:1的比重 亂數種子100
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.25, random_state=100)
lm =LinearRegression()
lm.fit(xTrain,yTrain)
# print('迴歸係數',lm.coef_)
# print('截距',lm.intercept_) #都會變動

# pred_train =lm.predict(xtrain)
pred_test =lm.predict(xTest)

# mse_train =np.mean((ytrain-pred_train)**2)
mse_test =np.mean((yTest-pred_test)**2)
print('--3:1 分割資料集--')
print('3:1,test_MSE:',mse_test)
# print('3:1,train_MSE:',mse_train) 
print('3:1,test_R-squared:',lm.score(xTest,yTest))
# print('3:1,train_R-squared:',lm.score(xtrain,ytrain))

#03  4:1的比重 亂數種子100
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=100)
lm =LinearRegression()
lm.fit(xTrain,yTrain)
# print('迴歸係數',lm.coef_)
# print('截距',lm.intercept_) #都會變動
# pred_train =lm.predict(xTrain)
pred_test =lm.predict(xTest)

# mse_Train =np.mean((xTrain-yTrain)**2)
mse_Test =np.mean((yTest-pred_test)**2)
print('--4:1 分割資料集--')
print('4:1,test_MSE:',mse_Test)
# print('4:1,train_MSE:',mse_Train) 
print('4:1,test_R-squared:',lm.score(xTest,yTest))
# print('4:1,train_R-squared:',lm.score(xTrain,yTrain))

#要選哪一種模組去做建模> 為何?





----------------------------------------------------------
邏輯練習04
# mean radius 平均半徑 mean texture 質地 mean perimeter 周長*
# mean area 面積 mean smoothness 平滑度  mean compactness 緊密度
# mean concavity 凹度 mean concave points 凹點  mean symmetry 對稱
# mean fractal dimension 分形維數  radius error 誤差  worst radius 壞的

import pandas as pd #讀取資料
import numpy as np #建立自己資料時要用
from sklearn import datasets #sklearn機器學習模式 只能處理數值 型態不是的要換型態
from sklearn import linear_model,preprocessing

breast_cancer =datasets.load_breast_cancer()#乳癌病患資料集
x =pd.DataFrame(breast_cancer.data ,columns =breast_cancer.feature_names) #自變數
#col =diabetes.feature_names
target =pd.DataFrame(breast_cancer.target, columns =['target'])
y =target['target']#因變數


logistic =linear_model.LogisticRegression(max_iter =4000) #max_iter 預設1000
#max_iter sklearn k 意味著處理每個疊代中的每個對象 當還有題是字 表示數字要再高一點
logistic.fit(x,y)
# print('迴歸係數',logistic.coef_)#數字越大 表示模組越好 所以用迴歸係數去選出 要接下去做的五個欄位
# print('截距',logistic.intercept_)

#混淆矩陣
print('混淆矩陣')
preds =logistic.predict(x)
print(pd.crosstab(breast_cancer['target'],preds)) 
print('全體的準確度 :',logistic.score(x,y))

#選出5個欄位--------------------------------------------------------------------
# logistic.coef#數字越大 表示模組越好 所以用迴歸係數去選出 要接下去做的五個欄位
five_C =pd.DataFrame(logistic.coef_,columns =breast_cancer.feature_names)
five_C=five_C.T #這樣才會轉成長條的
five=abs(five_C) #abs 絕對值 找出大小
five_abs=five.sort_values(0, ascending=False).index[0:5]
#.sort_values 排序只能使用這   xis=0==index==資料大小排序；axis=1==columns==索引大小
#預設ascending =True，即升序排列
print('選出五個迴歸係數較大的前五個 :\n',five_abs)

five_x =x[['worst concavity', 'texture error', 'mean radius', 'worst symmetry',
       'worst compactness']]

logistic =linear_model.LogisticRegression()
logistic.fit(five_x,y)
# print('迴歸係數',logistic.coef_)
# print('截距',logistic.intercept_)

#混淆矩陣 五個指標的準確度
print('混淆矩陣')
preds =logistic.predict(five_x)
print(pd.crosstab(breast_cancer['target'],preds)) 
print('五個指標的準確度 :',logistic.score(five_x,y))






--------------------------------------------
#機器學習5
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import neighbors
from sklearn import tree
from sklearn import linear_model
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns = iris.feature_names)
target = pd.DataFrame(iris.target, columns = ["target"])
y = target["target"]


# KNN

k = 50
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)
print("KNN建模正確率: ", knn.score(X,y))

# Decision Tree

dtree = tree.DecisionTreeClassifier(max_depth=3)
dtree.fit(X, y)
print("Decision Tree建模正確率: ", dtree.score(X,y))

#Logistic Regression

logistic = linear_model.LogisticRegression(max_iter=5000)
logistic.fit(X, y)
print("Logistic Regression建模正確率: ", logistic.score(X,y))

# =============================================================================
# split in 3:2    K Optimization
# =============================================================================

xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.4, random_state=50)
best_rate = 0

for k in range(1,91):  #150*0.6=90
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(xTrain, yTrain)
    rate = knn.score(xTest,yTest)
    
    print("K=%d  KNN建模正確率 = %f" % (k,rate))
    if best_rate < rate:
        best_rate = rate
        best_k = k
    
print("Best Rate =", best_rate)  
print("Best K=", best_k) 
    
-------------------------------------------------+
練習06
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model, neighbors, tree, cluster
from sklearn.linear_model import LinearRegression
import sklearn.metrics as sm

wine = datasets.load_wine()

X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
#print("K-means 演算法結果 : ", kmeans.labels_)

print("K-means 演算法結果正確率 : ", sm.accuracy_score(y, kmeans.labels_ ),"\n")

# 其他演算法

# k 演算法
k = 3
knn = neighbors.KNeighborsClassifier(n_neighbors = k)
knn.fit(X, y)

pred_knn = knn.predict(X)

print("原始資料集 K 演算法 模型預測機率 ", knn.score(X, y),"\n")

# 決策樹
dtree = tree.DecisionTreeClassifier(max_depth = 4)
dtree.fit(X, y)

pred_tree = dtree.predict(X)

print("原始資料集 決策樹 模型預測機率 ", dtree.score(X, y),"\n")

# 邏輯回歸
logistic = linear_model.LogisticRegression(max_iter = 3000)
logistic.fit(X, y)

pre_log = logistic.predict(X)

print("原始資料集 邏輯回歸 模型預測機率 ", logistic.score(X, y),"\n")

print("根據以上結果, 最適當演算法為邏輯回歸",
      "但也根據其他演算法所下值而有所變化 (max_depth, k ...)")































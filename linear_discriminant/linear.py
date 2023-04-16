from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# 创建一个LDA对象
lda = LinearDiscriminantAnalysis(n_components=1)

# 将数据拟合到LDA模型中
X = [(1,2), (2,3), (3,3), (4,5), (5,5), (1,0), (2,1), (3,1), (3,2), (5,3), (6,5)]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
lda.fit(X, y)

# 输出投影向量
print("投影向量：", lda.coef_)

# 输出样本在空间中的投影值
print("投影值：", lda.transform(X).flatten().tolist())
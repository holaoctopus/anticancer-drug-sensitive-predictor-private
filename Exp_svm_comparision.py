import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data/svm_accuracy.csv')
data.set_index('drug', inplace=True, drop=True)
print(data)
data.plot(kind='bar', width=0.9)
# data.boxplot()
# 设置坐标轴名称
plt.xlabel('')
plt.ylabel('Model Accuracy', fontsize=20)
plt.xticks(rotation=45, fontsize=15)
plt.title('drugs in CCLE dataset', fontsize=20)
# plt.savefig('image/svm_experiment.png')
plt.show()
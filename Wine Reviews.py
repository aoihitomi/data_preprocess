import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

data_file = ".\\winemag-data_first150k.csv"

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 读取数据集并保留需要的属性列
dataset = pd.read_csv(data_file, usecols=[1, 4, 5, 6, 7, 8, 9, 10])

# 频数统计
# params:
#   data:数据集
#   name:数据列名称
def data_summary(data, name):
    print(data[name].value_counts())

# 五数概括
# params:
#   data:数据集
#   name:数据列名称
def five_number_summary(data, name):
    datacol = data[name]
    min, max = datacol.min(), datacol.max()
    q1, q2, q3 = datacol.quantile(0.25), datacol.quantile(0.5), datacol.quantile(0.75)
    nan = datacol.isnull().sum()
    
    print("Five-number summary of data attribute {}:".format(name))
    print("Min value: " + str(min))
    print("Q1  value: " + str(q1))
    print("Q2  value: " + str(q2))
    print("Q3  value: " + str(q3))
    print("Max value: " + str(max))
    print("Number of missing value: " + nan)
    
# 条形图绘制
# params:
#   data:数据集
#   name:数据列名称
def bar_plot(data, name):
    summ = data[name].value_counts()
    summ.plot(color='r', kind='bar')
    plt.show()
    
# 盒图绘制
# params:
#   data:数据集
#   name:数据列名称
def box_plot(data, name):
    data[name].plot(kind='box')
    plt.show()
    
# 条形图对比
# params:
#   olddata:老数据集
#   newdata:新数据集
#   name:数据列名称
def barplot_comp(olddata, newdata, name):
    old_summ = olddata[name].value_counts()
    new_summ = newdata[name].value_counts()
    summs = pd.concat([old_summ, new_summ], axis=1)
    ax = summs.plot(colormap='Paired', kind='bar')
    ax.legend(['old', 'new'])
    plt.show()
    
# 盒图对比
# params:
#   olddata:老数据集
#   newdata:新数据集
#   name:数据列名称
def boxplot_comp(olddata, newdata, name):
    summs = pd.concat([olddata[name], newdata[name]], axis=1)
    summs.columns = ['old', 'new']
    ax = summs.plot(kind='box')
    plt.show()
    

# 将缺失部分剔除
# params:
#   data:数据集
def remove_missing_value(data):
    return data.dropna()

# 用出现频率最高值填补缺失值
# params:
#   data:数据集
def fill_with_most_frequent(data):
    new_data = data.copy()
    for column in new_data.columns:
        most_frequent = new_data[column].value_counts().index[0]
        new_data[column].fillna(most_frequent, inplace=True)
    return new_data

# 计算两数据点之间的欧氏距离
# params:
#   data:数据集
#   i:数据点1
#   j:数据点2
def distance(data, i, j):
    i_row = data.iloc[i]
    j_row = data.iloc[j]
    dist_factor = []
    if j_row.isna().any():
        return float('inf')
    
    for k in range(len(i_row)):
        if is_numeric_dtype(i_row[k]):
            dist_factor.append(abs(i_row[k] - j_row[k]))
        else:
            dist_factor.append(1 if i_row[k] == j_row[k] else 0)    
    dist = 0
    for k in range(len(dist_factor)):
        dist += dist_factor[k] * dist_factor[k]
    dist = pow(dist, 0.5)
    return dist

# 基于相似性填补数据集
# params:
#   data:数据集
def fill_with_similarity(data):
    index = []
    new_data = data.copy()
    nans = new_data.isna().any(axis=1)
    for i in range(len(nans)):
        if nans[i] == True:
            index.append(i)
    
    for i in index:
        dist = float('inf')
        sim_row = 0
        for j in range(new_data.shape[0]):
            if i == j:
                continue
            tmp_dist = distance(new_data, i, j)
            if tmp_dist < dist:
                dist = tmp_dist
                sim_row = j
        new_data.iloc[i] = new_data.iloc[sim_row]
    return new_data

# 基于相关关系填充
# params:
#   data:数据集
def fill_with_corr(data):
    new_data = data.copy()
    numeric_col = ['points', 'price']
    for column in new_data.columns:
        if column in numeric_col:
            new_data[column].fillna(new_data[column].mean(), inplace=True)
        else:
            most_frequent = new_data[column].value_counts().index[0]
            new_data[column].fillna(most_frequent, inplace=True)
    return new_data


    
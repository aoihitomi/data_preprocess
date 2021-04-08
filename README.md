# 数据探索性分析与数据预处理

选择数据集：
+ [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews)
+ [Trending YouTube Video Statistics](https://www.kaggle.com/datasnaek/youtube-new)

使用方法：
将数据集与代码文件放入同一目录下，然后可以根据需要调用代码文件中的相应函数进行显示。

数据摘要函数：
```python
# 频数统计
# params:
#   data:数据集
#   name:数据列名称
def data_summary(data, name)

# 五数概括
# params:
#   data:数据集
#   name:数据列名称
def five_number_summary(data, name)
```
数据可视化函数：
```python
# 条形图绘制
# params:
#   data:数据集
#   name:数据列名称
def bar_plot(data, name)
    
# 盒图绘制
# params:
#   data:数据集
#   name:数据列名称
def box_plot(data, name)
```

四种数据预处理填补缺失值函数：
```python
# 将缺失部分剔除
# params:
#   data:数据集
def remove_missing_value(data)

# 用出现频率最高值填补缺失值
# params:
#   data:数据集
def fill_with_most_frequent(data)

# 基于相似性填补数据集
# params:
#   data:数据集
def fill_with_similarity(data)

# 基于相关关系填充
# params:
#   data:数据集
def fill_with_corr(data)
```

用于填补缺失值后进行新旧数据集对比函数：
```python
# 条形图对比
# params:
#   olddata:老数据集
#   newdata:新数据集
#   name:数据列名称
def barplot_comp(olddata, newdata, name)
    
# 盒图对比
# params:
#   olddata:老数据集
#   newdata:新数据集
#   name:数据列名称
def boxplot_comp(olddata, newdata, name)
```

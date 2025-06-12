import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# name = ['lee', 'hong', 'park', 'yoon']
# score = [230, 250, 300, 300]
# age = [19, 26, 22, 29]
#
# data_df = pd.DataFrame(index = [101, 102, 103, 104])
# data_df['이름'] = name
# data_df['점수'] = score
# data_df['나이'] = age
# data_df.to_csv('../data/data_score.csv')
#
# print(data_df)

# df = pd.read_csv('../data/nations.csv', index_col=0)
# print(df.head())
# print(df.tail())
# print(df[:3])
# print(df.loc['KR'])
# print(list(df))

# df['population'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm'))
# colors = sns.color_palette('Blues', len(df))
#('line', 'bar', 'barh', 'kde', 'density', 'area', 'hist', 'box', 'pie', 'scatter', 'hexbin')
# df['density'].plot(kind='barh', color=colors)
# plt.legend()
# plt.show()

# df['density'] = df['population'] / df['area']
# print(df)

weather = pd.read_csv('../data/weather.csv', encoding='cp949', index_col=0)
weather = weather.dropna()
print(weather.count())
weather['평균기온(°C)'].plot(kind='line', color=('red'))
weather['최대 풍속(m/s)'].plot(kind='line', color=('green'))
weather['평균 풍속(m/s)'].plot(kind='line', color=('blue'))
plt.legend()
plt.show()
print(weather)
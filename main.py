import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("gapminder.csv")
data_frame.head()

data_frame.shape
data_frame.columns
data_frame.dtypes
data_frame.describe()

data_frame['continent'].unique()
data_frame.groupby('continent')['country'].nunique()

oceania = data_frame.loc[data_frame['continent'] == "Oceania"]
oceania.head()
oceania['continent'].unique()

plt.plot(data_frame.groupby('year')['life_exp'].mean())
plt.title('Life Expectancy per year')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.show()

plt.plot(data_frame.groupby('year')['gdp_cap'].mean())
plt.title('Per Capita Income per year')
plt.xlabel('Year')
plt.ylabel('Per Capita Income')
plt.show()

plt.plot(data_frame.groupby('year')['population'].mean())
plt.title('Population per year')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()
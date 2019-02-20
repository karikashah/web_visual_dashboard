import pandas as pd

cities = pd.read_csv('./cities.csv')
print(cities.head())

cities.to_html('city.html', index=False)




"""Feature is nothing but a input data
x value or input data or independent data or feature data

Process 1: Converting categorical data into numerical data"""

import pandas as pd

data = pd.read_csv("diamonds.csv")
print(data.dtypes)

data.dropna(inplace=True)

finding_various_categories = data['cut'].unique()
print(finding_various_categories)

finding_various_categories_count = data['cut'].nunique()
print(finding_various_categories_count)

finding_category_count = data['cut'].value_counts()
print(finding_category_count)

# print(data.head())
# print("---------------------------------------------------------------------")
# data['cut'] = data['cut'].map({"Premium":5,"Ideal":1,"Very Good":3,"Good":4,"Fair":2})
# print(data.head())

# from sklearn.preprocessing import LabelEncoder
# print(data.head())
# print("====================")
# label_encoding_object = LabelEncoder()
# data['cut'] = label_encoding_object.fit_transform(data['cut'])
# print(data.head())

# from sklearn.preprocessing import OrdinalEncoder
# print(data.head())
# print("====================")
# label_encoding_object = OrdinalEncoder()
# data['cut'] = label_encoding_object.fit_transform(data[['cut']])
# print(data.head())
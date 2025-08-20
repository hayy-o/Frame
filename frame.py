import pandas as pd

# DataFrame from dictionary
data = {"name": ['rahma', 'hayaa', 'engy', 'sara'], "age": [21, 20, 19, 21]}
df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)
print(" ")

# DataFrame from list with column names
data = [['rahma', 21], ['hayaa', 20], ['engy', 19], ['sara', 21]]
df2 = pd.DataFrame(data, columns=['name', 'age'])
print("DataFrame from list:")
print(df2)
print(" ")

# Load dataset once
dataset = pd.read_csv("disney_princess_popularity_dataset_300_rows.csv")

# Print first 15 rows
print("First 15 rows:")
print(dataset.head(15))
print(" ")

# Print one column
print("RottenTomatoesScore column:")
print(dataset['RottenTomatoesScore'])
print(" ")

# Print multiple columns
print("RottenTomatoesScore and FirstMovieYear columns:")
print(dataset[['RottenTomatoesScore', 'FirstMovieYear']])
print(" ")

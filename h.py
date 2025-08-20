# Disney Princess Popularity - Visualization Examples

import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
dataset = pd.read_csv("disney_princess_popularity_dataset_300_rows.csv")

# 1) Histogram
dataset.hist()
plt.show()

# 2) First 15 rows line plot
d = dataset.head(15)
d.plot()
plt.show()

# 3) First 10 rows - plot specific column
d = dataset.head(10)
d.plot(y="InstagramFanPages")
plt.show()

# 4) First 5 rows - plot two columns against each other
d = dataset.head(5)
d.plot(x="FirstMovieTitle", y="FirstMovieYear")
plt.show()

# 5) Density plot
dataset.plot(kind='density')
plt.show()

# 6) Density plots for all columns in subplots
dataset.plot(kind='density', subplots=True, layout=(4,3), figsize=(10,8))
plt.show()

# 7) Bar plot - first 20 values of MovieRuntimeMinutes
data = dataset['MovieRuntimeMinutes']
data.head(20).plot(kind="bar")
plt.show()

# 8) Box plot for MovieRuntimeMinutes
data.plot(kind="box")
plt.show()

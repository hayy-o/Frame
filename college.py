# Step 1, 2, 3: Data Processing
import pandas as pd

# قراءة البيانات
df = pd.read_csv('disney_princess_popularity_dataset_300_rows.csv')

# عرض البيانات الأساسية
print("Dataset Preview:")
print(df.head())          # عرض أول 5 صفوف بدل الطباعة الكاملة
print("\nData Types:")
print(df.dtypes)
print("\nStatistical Summary:")
print(df.describe())
print("\n")

# Step 4: Finding missing values in each column
print("Missing Values:")
print(df.isna().sum())
print("\n")

# Step 5: Dropping rows containing missing values
df_clean = df.dropna()
print("Missing Values After Dropping Rows:")
print(df_clean.isna().sum())
print("\n")

# Step 6: Checking for duplicates
print("Duplicate Rows (Boolean):")
print(df_clean.duplicated())
print("\n")

# Step 7: Removing duplicates
df_clean = df_clean.drop_duplicates()
print("Data After Removing Duplicates:")
print(df_clean)

# (اختياري) حفظ النسخة النظيفة في ملف جديد
df_clean.to_csv('disney_princess_popularity_clean.csv', index=False)
print("\nClean dataset saved as 'disney_princess_popularity_clean.csv'")

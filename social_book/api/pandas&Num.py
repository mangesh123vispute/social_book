
import pandas as pd
import numpy as np

# Task 2: 
data = {
    'Column1': np.random.randint(1, 100, size=10),
    'Column2': np.random.randint(1, 100, size=10),
    'Column3': np.random.randint(1, 100, size=10)
}
df = pd.DataFrame(data)
print("Task 2: DataFrame Created (10x3)\n", df, "\n")

# Task 3: 
filter_value = 50
filtered_df = df[df['Column1'] > filter_value]
print(f"Task 3: DataFrame Filtered (Column1 > {filter_value})\n", filtered_df, "\n")

# Task 4: 
filtered_df_2cols = df[['Column1', 'Column2']]
print("Task 4: DataFrame with 2 Columns (Column1 and Column2)\n", filtered_df_2cols, "\n")

# Task 5:
df['Column2'] = df['Column2'].apply(lambda x: 80 if x > 80 else x)
print("Task 5: DataFrame After Replacing Values in Column2 (values > 80 are replaced with 80)\n", df, "\n")

# Task 6: 
data2 = {
    'Column1': np.random.randint(1, 100, size=10),
    'Column2': np.random.randint(1, 100, size=10),
    'Column3': np.random.randint(1, 100, size=10)
}
df2 = pd.DataFrame(data2)

appended_df = pd.concat([df, df2], ignore_index=True)
print("Task 6: Appended DataFrame\n", appended_df)

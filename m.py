import pandas as pd

def read_dish_csv(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            fields = line.strip().split(',')
            data.append(fields)
    # Find max length
    if data:
        max_len = max(len(row) for row in data)
        # Pad with None
        for row in data:
            while len(row) < max_len:
                row.append(None)
    return pd.DataFrame(data)

df1 = read_dish_csv("metadata/dish_metadata_cafe1.csv")
df2 = read_dish_csv("metadata/dish_metadata_cafe2.csv")

df = pd.concat([df1, df2], ignore_index=True)

print("Shape of combined DataFrame:", df.shape)
print("First 5 rows, first 10 columns:")
print(df.iloc[:5, :10])
print("Columns:", list(df.columns))

# Save to CSV for easier viewing
df.to_csv("combined_dish_metadata.csv", index=False)
print("Saved combined data to combined_dish_metadata.csv")

import pandas as pd
df = pd.read_csv("combined_dish_metadata.csv")
df = df[["0", "1", "2", "3", "4", "5"]].dropna()
df.columns = ["dish_id", "total_mass", "total_calories", "total_fat", "total_carb", "total_protein"]

# Apply nutrition mapping: calculate per 100g values
df["calories_per_100g"] = df["total_calories"] / (df["total_mass"] / 100)
df["fat_per_100g"] = df["total_fat"] / (df["total_mass"] / 100)
df["carb_per_100g"] = df["total_carb"] / (df["total_mass"] / 100)
df["protein_per_100g"] = df["total_protein"] / (df["total_mass"] / 100)

print(df.head())
print(df.shape)

# Save the cleaned data with per 100g values to a new CSV
df.to_csv("cleaned_nutritional_data_per_100g.csv", index=False)
print("Saved cleaned data with per 100g values to cleaned_nutritional_data_per_100g.csv")
nutrition_map = df.set_index("dish_id").to_dict("index")
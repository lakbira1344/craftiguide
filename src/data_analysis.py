import pandas as pd
DATA_PATH = "data/craftiguide_dataset_training.csv"
df = pd.read_csv(DATA_PATH)
print(df.head())
print(df.shape)
print(df.info())
print(df[["text", "category"]].isna().sum())
print("Doublons :", df["text"].duplicated().sum())
print(df["category"].value_counts())
    
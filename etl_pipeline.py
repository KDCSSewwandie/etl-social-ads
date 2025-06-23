import pandas as pd
import os

def extract(file_path):
    # Load the raw dataset
    df = pd.read_csv(file_path)
    return df

def transform(df):
    # Add an 'AgeGroup' column based on 'Age' ranges
    df['AgeGroup'] = pd.cut(df['Age'], bins=[18, 25, 35, 45, 60], labels=["18-25", "26-35", "36-45", "46-60"])
    return df

def load(df, output_path='data/cleaned_social_ads.csv'):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save the transformed data to CSV
    df.to_csv(output_path, index=False)
    print("✅ Data saved to", output_path)

def etl_pipeline():
    input_path = "data/social_ads.csv"
    df = extract(input_path)
    df = transform(df)
    load(df)

if __name__ == "__main__":
    etl_pipeline()

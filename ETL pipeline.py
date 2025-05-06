import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

# Step 0: Create sample data
def create_sample_data():
    data = {
        'age': [25, 30, np.nan, 40, 22],
        'salary': [50000, 60000, 52000, np.nan, 58000],
        'city': ['New York', 'Los Angeles', 'New York', 'Chicago', None],
        'gender': ['Male', 'Female', 'Female', None, 'Male']
    }
    df = pd.DataFrame(data)
    df.to_csv("sample_input.csv", index=False)
    print("Sample input CSV created.")
    return df

# Step 1: Extract data
def extract_data(file_path):
    return pd.read_csv(file_path)

# Step 2: Preprocess data
def preprocess_data(df):
    numeric_features = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = df.select_dtypes(include=['object']).columns

    numeric_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer([
        ('num', numeric_pipeline, numeric_features),
        ('cat', categorical_pipeline, categorical_features)
    ])

    processed_data = preprocessor.fit_transform(df)
    return processed_data, preprocessor

# Step 3: Load transformed data
def load_transformed_data(transformed_data, output_path='transformed_output.csv'):
    if hasattr(transformed_data, 'toarray'):
        df_transformed = pd.DataFrame(transformed_data.toarray())
    else:
        df_transformed = pd.DataFrame(transformed_data)
    df_transformed.to_csv(output_path, index=False)
    print(f"Transformed data saved to {output_path}")

# Run the ETL process
def run_etl_pipeline():
    create_sample_data()
    df = extract_data("sample_input.csv")
    transformed_data, _ = preprocess_data(df)
    load_transformed_data(transformed_data)

# Run
if __name__ == "__main__":
    run_etl_pipeline()

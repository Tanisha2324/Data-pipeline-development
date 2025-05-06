# Data-pipeline-development

 *COMPANY*: CODTECH IT SOLUTIONS
 
 *NAME*: TANISHA ADISHYA
 
 *Intern ID*: CT04DL950
 
 *DOMAIN*: DATA SCIENCE
 
 *DURATION*: FOUR WEEKS
 
 *MENTOR*: NEELA SANTOSH KUMAR
 
 ### Overview

 # ETL Pipeline with Pandas and Scikit-learn

Hi! This is a simple Python script I created to demonstrate a basic ETL (Extract, Transform, Load) pipeline using `pandas` and `scikit-learn`.

### 🚀 What This Script Does

1. **Extract**  
   I start by creating a sample dataset (`sample_input.csv`) that includes missing values and both numeric and categorical columns.

2. **Transform**  
   I clean the data using:
   - **SimpleImputer** to handle missing values
   - **StandardScaler** to normalize numeric columns
   - **OneHotEncoder** to encode categorical features

3. **Load**  
   Finally, I save the cleaned and transformed data into `transformed_output.csv`.

---

### 📂 Files

- `etl_pipeline.py`: The main Python script containing the ETL logic.
- `sample_input.csv`: Automatically generated sample input file.
- `transformed_output.csv`: Output file containing the cleaned and transformed data.

---

### 🛠️ Requirements

You can install the required libraries using pip:

```bash
pip install pandas scikit-learn numpy


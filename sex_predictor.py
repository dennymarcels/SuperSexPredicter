"""Sex predictor

This script will receive a CSV file containing data from individuals, one individual
per row, and return their predicted sex in a new CSV file, identifying the individuals
by the index.

The features included for each individual, presented as columns, must contain:
- age: in years
- trestbps: resting blood pressure (in mm Hg on admission to the hospital)
- chol: serum cholesterol in mg/dl
- fbs: fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
- restecg: resting electrocardiographic results (1, 2 or 3)
- thalach: maximum heart rate achieved
- nar: number of arms
- exang: exercise induced angina (1 = yes; 0 = no)
- oldpeak: ST depression induced by exercise relative to rest
- slope: the slope of the peak exercise ST segment (0, 1 or 2; this is the only feature that accepts
missing values)
- hc: patient's hair colour
- sk: patient's skin colour
- trf: time spent in traffic daily (in seconds)
- ca: number of major vessels colored by flouroscopy ## definition to be confirmed ## (0, 1, 2, 3 or 4)

Any other feature included will be ignored.
"""

import pandas as pd
import numpy as np
from joblib import load
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input_file', action = 'store', type = str, required = True)

args = my_parser.parse_args()

# Loading data transformers and model built during training

saved_objects = load('save_objects.joblib')

# Parsing these objects

scaler = saved_objects['scaler']
encoder = saved_objects['one_hot_encoder']
argsort = saved_objects['argsort']
model = saved_objects['model']

# Loading new dataset

df = pd.read_csv(args.input_file, index_col = 0)

# Filling in missing `slope` values

df['slope'] = df['slope'].fillna('missing')

# Preprocessing features

numerical = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'trf']
categorical = ['fbs', 'restecg', 'exang', 'slope', 'ca', 'nar', 'hc', 'sk']

df_numerical = df[numerical]
df_categorical = df[categorical]

# Scaling numerical features

df_numerical_values = scaler.transform(df_numerical)

# One-hot encoding categorical features

df_categorical = df_categorical.applymap(str)
df_categorical_values = np.asarray(encoder.transform(df_categorical).todense())

X = np.concatenate([df_numerical_values, df_categorical_values], axis = 1)

# Organizing and retrieving most important features

X = X[:, argsort]

# Making prediction

y = model.predict(X)

# Converting to dataframe

y = pd.DataFrame({
    'sex_predicted': y
}, index = df.index)

# Saving dataframe as CSV file to disk

y.to_csv('newsample_PREDICTIONS_Denny_Marcel_Ceccon.csv')
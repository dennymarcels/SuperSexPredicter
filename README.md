# SUPER SEX PREDICTER

This repository is dedicated to a sex classifier that is based on some clinical and demographic information.

The repository contains the following files:
- *Data exploration and model desing.ipynb*: Jupyter Notebook with data exploration, manipulation and model design.
- *sex_predictor.py*: Python script to run the predictor on a new dataset.
- *requirements.txt*: file listing the dependencies necessary to run both the script and the data exploration/model design notebook.
- *save_objects.joblib*: file containing the model and other data transformation Python objects needed to make predictions.
- *newsample.csv*: a sample of the original dataset to be used as an example with the predictor. The original dataset is not provided.

In order to run the script, first clone this repository and run `pip install -r requirements.txt`. The script is run with `python sex_predictor.py --input_file FILE_NAME`. You can use the file `newsample.csv` to test it. It will produce a new csv file with the predictions, in the same folder. Each individual in the new dataset is mapped to the same row in the output file.

The csv file submitted to the script must represent each individual in a new row, and must have the following columns:
- age: in years
- trestbps: resting blood pressure on admission to the hospital (in mm Hg)
- chol: serum cholesterol (in mg/dl)
- fbs: fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- restecg: resting electrocardiographic results (1, 2 or 3)
- thalach: maximum heart rate achieved (in bpm)
- nar: number of arms
- exang: exercise induced angina (1 = yes, 0 = no)
- oldpeak: ST depression induced by exercise relative to rest
- slope: the slope of the peak exercise ST segment (0, 1 or 2; this is the only feature that accepts missing values, in case they are not available)
- hc: patient's hair colour (0, 1 or 2)
- sk: patient's skin colour (0, 1, 2 or 3)
- trf: time spent in traffic daily (in seconds)
- ca: number of major vessels colored by flouroscopy ## definition to be confirmed ## (0, 1, 2, 3 or 4)

Other features might be present, but they will be ignored.

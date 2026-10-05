
import streamlit as st
import sklearn
import xgboost
import joblib
import pandas as pd

st.write("Python environment check")
st.write("scikit-learn:", sklearn.__version__)
st.write("XGBoost:", xgboost.__version__)
st.write("joblib:", joblib.__version__)
st.write("pandas:", pd.__version__)

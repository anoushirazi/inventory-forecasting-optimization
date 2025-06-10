import numpy as np
import pandas as pd

# Function to calculate mean absolute error
def mean_absolute_error(y_true, y_pred):
    """
    Calculate Mean Absolute Error (MAE)
    """
    return np.mean(np.abs(y_true - y_pred))

# Function to calculate root mean squared error
def root_mean_squared_error(y_true, y_pred):
    """
    Calculate Root Mean Squared Error (RMSE)
    """
    return np.sqrt(np.mean((y_true - y_pred)**2))

# Function to calculate safety stock
def calculate_safety_stock(forecast_error, multiplier=1.5):
    """
    Calculate safety stock given forecast error and a multiplier.
    Default multiplier is 1.5.
    """
    return multiplier * np.std(forecast_error)

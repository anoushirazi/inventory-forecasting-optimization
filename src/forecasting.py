from fbprophet import Prophet
import pandas as pd

# Function to forecast using Prophet
def prophet_forecast(df, periods=12):
    """
    Forecast sales using Prophet, which is a time-series forecasting model.
    
    df: DataFrame with 'Date' as 'ds' and 'Total Amount' as 'y'
    periods: Number of future periods to forecast
    """
    df = df.rename(columns={'Date': 'ds', 'Total Amount': 'y'})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods, freq='W')
    forecast = model.predict(future)
    return forecast

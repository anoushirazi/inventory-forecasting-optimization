import numpy as np

# Function to calculate lead time demand
def calculate_lead_time_demand(forecasted_sales):
    """
    Calculate the lead time demand, which is the mean of the forecasted sales.
    
    forecasted_sales: Array of predicted sales over a period of time.
    """
    return np.mean(forecasted_sales)

# Function to calculate reorder point
def calculate_reorder_point(lead_time_demand, safety_stock):
    """
    Calculate reorder point by adding lead time demand and safety stock.
    
    lead_time_demand: Mean of forecasted sales.
    safety_stock: Standard deviation of forecast error or safety buffer.
    """
    return lead_time_demand + safety_stock

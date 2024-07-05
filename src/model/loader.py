import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def load_and_process_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)
    
    # Convert date column to datetime
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Sort data by date
    data = data.sort_values(by='Date')
    
    # Add day of the week column
    data['Day of Week'] = data['Date'].dt.day_name()
    
    # Classify daily changes as positive or negative
    data['Positive'] = data['Change %'].str.rstrip('%').astype('float') / 100 > 0
    
    # Calculate percentage of positive and negative days per day of the week
    positive_days = data.groupby('Day of Week')['Positive'].mean() * 100
    negative_days = 100 - positive_days
    
    # Create a DataFrame with the calculated statistics
    weekly_stats = pd.DataFrame({
        'Positive Days (%)': positive_days,
        'Negative Days (%)': negative_days
    }).sort_index()
    
    # Filter out weekends and reorder the data
    if 'Sunday' in weekly_stats.index:
        weekly_stats = weekly_stats.drop('Sunday')
    if 'Saturday' in weekly_stats.index:
        weekly_stats = weekly_stats.drop('Saturday')
    order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    ordered_stats = weekly_stats.loc[order]
    
    return ordered_stats
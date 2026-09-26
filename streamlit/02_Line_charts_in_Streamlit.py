import time
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

rows = np.random.randn(1,1)

'Growing Line Chart:'
# Create an empty placeholder container
chart_placeholder = st.empty()

# Create a history array to store all data points over time
data_history = rows

for i in range(1, 100):
    # Calculate the next data point relative to the last one
    new_rows = rows + np.random.randn(1, 1)
    
    # Append the new row to our historical data array
    data_history = np.vstack([data_history, new_rows])
    
    # Re-render the line chart inside the placeholder with full history
    chart_placeholder.line_chart(data_history)
    
    # Update current row state and pause
    rows = new_rows
    time.sleep(0.05)

values = np.random.rand(10)
'matplotlibs Line Chart:'
fig, ax = plt.subplots()
ax.plot(values)
st.pyplot(fig)

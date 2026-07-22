import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np

# Download historical stock data
stock = yf.download("AAPL", period="1y")

# Use the day number as input
X = np.arange(len(stock)).reshape(-1, 1)

# Use closing prices as output
y = stock["Close"].values

# Train the AI model
model = LinearRegression()
model.fit(X, y)

# Predict the next 7 days
future_days = np.arange(len(stock), len(stock) + 7).reshape(-1, 1)
predictions = model.predict(future_days)

print("Predicted Prices:")
for i, price in enumerate(predictions, start=1):
    print(f"Day {i}: ${price:.2f}")

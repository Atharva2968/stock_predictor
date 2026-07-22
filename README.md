# AI Stock Market Predictor

Final project for the Building AI course

## Summary

AI Stock Market Predictor is a machine learning application that predicts future stock prices using historical market data. It helps users understand market trends and supports better investment decisions.

## Background

The stock market changes constantly, making it difficult for investors to predict future prices. Many beginners do not have the knowledge or tools to analyze market trends effectively.

This project aims to solve the following problems:

- Predict future stock prices using AI.
- Help beginners understand market trends.
- Reduce manual analysis.
- Provide a simple and easy-to-use prediction tool.

My interest in artificial intelligence and finance inspired me to create this project.

## How is it used?

The user enters a stock symbol such as AAPL, TSLA, or RELIANCE.

The application then:

1. Downloads historical stock market data.
2. Processes and cleans the data.
3. Trains a machine learning model.
4. Predicts future stock prices.
5. Displays the prediction.

Example:

```python
symbol = input("Enter Stock Symbol: ")

prediction = predict_price(symbol)

print("Predicted Price:", prediction)
```

The project is intended for:

- Students
- Investors
- Researchers
- Anyone interested in stock market analysis

## Data sources and AI methods

### Data Sources

- Yahoo Finance
- Public stock market datasets

### AI Methods

- Machine Learning
- Linear Regression
- Time Series Analysis
- Data Preprocessing

### Technologies

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-learn | Machine Learning |
| yFinance | Stock Market Data |

Useful links:

- https://finance.yahoo.com/
- https://pypi.org/project/yfinance/

## Challenges

The stock market is influenced by many unpredictable factors such as economic conditions, political events, and breaking news. Therefore, predictions cannot be completely accurate.

This project is designed for learning purposes and should not be used as financial advice.

## What next?

Future improvements include:

- Deep Learning models such as LSTM
- News sentiment analysis
- Cryptocurrency prediction
- Mobile application
- Real-time stock alerts
- Cloud deployment

## Acknowledgments

- University of Helsinki
- Reaktor Innovations
- Yahoo Finance
- Python community
- Pandas
- NumPy
- Scikit-learn

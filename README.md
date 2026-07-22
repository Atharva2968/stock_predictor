# AI Stock Market Predictor

Final project for the Building AI course

## Summary

AI Stock Market Predictor is a machine learning application that predicts future stock prices using historical market data. It helps users understand stock trends through AI-powered forecasting and simple visualizations.

---

## Background

Investing in the stock market is difficult because prices change every second due to economic conditions, news, and global events. Beginners often struggle to understand these trends and make informed decisions.

This project aims to solve these problems:

- 📉 Difficulty predicting future stock prices.
- 🤔 Lack of knowledge about market trends.
- ⏳ Time-consuming manual analysis.
- 📊 Limited access to simple AI-based prediction tools.

### Why I chose this project

I am interested in Artificial Intelligence, Machine Learning, and Finance. This project combines these fields into a practical AI application that demonstrates how machine learning can be used to analyze real-world financial data.

---

## How is it used?

The user enters a stock symbol such as **AAPL**, **TSLA**, or **RELIANCE**.

The application then:

1. 📥 Downloads historical stock market data.
2. 🧹 Cleans and prepares the data.
3. 🤖 Trains a machine learning model.
4. 📈 Predicts future stock prices.
5. 📊 Displays the prediction and charts.

### Example

```python
symbol = input("Enter Stock Symbol: ")

prediction = predict_price(symbol)

print("Predicted Price:", prediction)
```

### Users

- 🎓 Students
- 💼 Investors
- 📊 Financial Analysts
- 🤖 AI Enthusiasts

---

## Data sources and AI methods

### Data Sources

- 📈 Yahoo Finance Historical Data
- 🌐 Public Stock Market Data

### AI Methods

- 🤖 Machine Learning
- 📊 Linear Regression
- 📈 Time Series Analysis
- 🧹 Data Preprocessing

### Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-learn | Machine Learning |
| Matplotlib | Data Visualization |
| yFinance | Download Stock Data |

---

## Challenges

This project cannot predict stock prices with complete accuracy because financial markets are influenced by many unpredictable factors.

Some limitations include:

- 🌍 Global economic events
- 📰 Breaking news
- 💰 Market volatility
- 📉 Unexpected market crashes
- 📊 Limited historical data

⚠️ This project is intended for educational purposes only and should not be used as financial advice.

---

## What next?

Future improvements include:

- 🧠 Deep Learning (LSTM)
- 🤖 Transformer Models
- 📰 News Sentiment Analysis
- 💬 Social Media Analysis
- 📱 Mobile Application
- ☁️ Cloud Deployment
- 🔔 Real-Time Stock Alerts
- 💹 Cryptocurrency Prediction

---

## Acknowledgments

- ❤️ University of Helsinki for the Building AI course.
- ❤️ Reaktor Innovations for developing the course.
- ❤️ Yahoo Finance for providing historical stock market data.
- ❤️ Python, Pandas, NumPy, and Scikit-learn communities for their open-source libraries.

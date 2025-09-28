# MachineLearningREPO
# Simple Machine Learning Example – Linear Regression

This repository demonstrates the simplest example of machine learning: **linear regression**.

We use `scikit-learn` to fit a line between house size (square feet) and house price.  
The model then predicts the price of a house given its size.

---

## 🔍 How It Works
1. **Dataset**: A small dataset of house sizes and prices.
2. **Feature/Target Split**:  
   - `X` = House size (input)  
   - `y` = House price (output we want to predict)  
3. **Training**: We fit a `LinearRegression` model from scikit-learn.
4. **Prediction**: We ask the model to predict the price of a new house (e.g., 1800 sq ft).
5. **Visualization**: We plot the actual data points and the regression line.

This demonstrates how machine learning can "learn" from past examples and make predictions about new data.

---

## ⚙️ Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/ml-example.git
   cd ml-example

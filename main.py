#!/usr/bin/env python3
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Create simple dataset (House size vs. Price)
data = {
    "size": [500, 750, 1000, 1250, 1500],  # in square feet
    "price": [150000, 200000, 250000, 300000, 350000]  # in dollars
}
df = pd.DataFrame(data)

# Step 2: Prepare features (X) and target (y)
X = df[["size"]]  # Features must be 2D
y = df["price"]

# Step 3: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 4: Make prediction
predicted_price = model.predict([[1800]])
print(f"Predicted price for 1800 sq ft house: ${predicted_price[0]:,.2f}")

# Step 5: Visualize results
plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, model.predict(X), color="red", label="Regression line")
plt.xlabel("House size (sq ft)")
plt.ylabel("Price ($)")
plt.legend()
plt.show()


if __name__ == "__main__":
    train_and_predict()
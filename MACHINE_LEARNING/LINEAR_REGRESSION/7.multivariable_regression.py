import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def main():
    # Generate sample data
    np.random.seed(0)
    X = np.random.rand(100, 3) # 100 samples, 3 features
    y = 2 + 3*X[:, 0] + 1.5*X[:, 1] + 0.5*X[:, 2] + np.random.randn(100)*0.1
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Print results
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    print("Mean squared error: {:.4f}".format(mse))
    print("R-squared score: {:.4f}".format(r2))
    
    # Example prediction
    new_data = np.array([[0.5, 0.5, 0.5]])
    prediction = model.predict(new_data)
    print("Prediction for [0.5, 0.5, 0.5]:", prediction[0])
    
    # Plotting
    plt.figure(figsize=(12, 5))
    
    # Predicted vs Actual plot
    plt.subplot(121)
    plt.scatter(y_test, y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Predicted vs Actual Values")
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()
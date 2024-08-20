
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def main():
    # Load the dataset
    data = pd.read_csv("training_data.csv")
    
    # Display the first few rows and descriptive statistics (for debugging purposes)
    print(data.head())
    print(data.describe())
    
    # Define features and target variable
    X = data.iloc[:, [0]].values
    Y = data.iloc[:, 1].values
    
    # Check for NaN values in Y
    if np.isnan(Y).sum() > 0:
        print(f"Found {np.isnan(Y).sum()} NaN values in Y. Handling them by dropping corresponding rows.")
        # Removing rows where Y is NaN
        mask = ~np.isnan(Y)
        X = X[mask]
        Y = Y[mask]
    
    # Split the dataset into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, Y_train)
    
    # Make predictions
    Y_pred = model.predict(X_test)
    
    # Plotting the results
    plt.scatter(X_test, Y_test, label='Actual Datapoints')
    plt.scatter(X_test, Y_pred, label='Predicted Datapoints', c='green')
    plt.plot(X_train, model.predict(X_train), label='Regression Line', color='red')
    plt.xlabel('Years Of Experience')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()
    
    # Evaluate the model
    mse = mean_squared_error(Y_test, Y_pred)
    r2 = r2_score(Y_test, Y_pred)
    
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 score: {r2}")

if __name__ == '__main__':
    main()

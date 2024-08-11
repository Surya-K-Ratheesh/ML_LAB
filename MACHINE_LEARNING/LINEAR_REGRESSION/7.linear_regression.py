import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv("salary_data.csv")
    data.head()
    data.describe()
    
    X = data.iloc[:, [0]].values
    Y = data.iloc[:, 1]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
    
    model = LinearRegression()
    
    model.fit(X_train, Y_train)
    
    Y_pred = model.predict(X_test)
    
    plt.scatter(X_test, Y_test, label = 'Actual Datapoints')
    plt.scatter(X_test, Y_pred, label = 'Predicted Datapoints', c = 'green')
    plt.plot(X_train, model.predict(X_train), label = 'Regression Line', color = 'red')
    plt.xlabel('Years Of Experience')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()
    
    mse = mean_squared_error(Y_test, Y_pred)
    r2 = r2_score(Y_test, Y_pred)
    
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 score: {r2}")


if __name__ == '__main__':
    main()
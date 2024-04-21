import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class HousePricePredictor:
    df = pd.read_csv("GUI/static/csv/data_model.csv")
    # set the target and predictors
    y = df.LogOfPrice  # target
    # use only those input features with numeric data type 
    df_temp = df.select_dtypes(include=["int64","float64"]) 
    X = df_temp.drop(["LogOfPrice"],axis=1)  # predictors
    # split the dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .25, random_state = 3)
    
    def __init__(self):
        pass

    def linearRegression(self):
        lr = LinearRegression()
        # fit optimal linear regression line on training data, this performs gradient descent under the hood
        lr.fit(X_train, y_train)
        # given our model and our fit, predict y_values using X_test set
        yr_hat = lr.predict(X_test)


    def lassoRegression(self):
        pass

    def ridgeRegression(self):
        pass

    def randomForest(self):
        pass

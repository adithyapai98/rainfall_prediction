import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load the data from the CSV file
data = pd.read_csv('C:/Users/adith/Desktop/Analysis/weather_clean.csv')

# Select the features to be used in the model
features = list(data.columns)
features.remove('precipitation_sum')

# Split the data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Fit a linear regression model to the training data
model = LinearRegression()
model.fit(train_data[features], train_data['precipitation_sum'])

# Evaluate the model on the testing data
predictions = model.predict(test_data[features])
mae = mean_absolute_error(test_data['precipitation_sum'], predictions)
rmse = mean_squared_error(test_data['precipitation_sum'], predictions, squared=False)
score = model.score(test_data[features], test_data['precipitation_sum'])
print("R-squared score: {:.2f}".format(score))
print("Mean Absolute Error: {:.2f}".format(mae))
print("Root Mean Squared Error: {:.2f}".format(rmse))

# Generate a scatter plot of actual vs predicted values
plt.style.use('seaborn')
plt.scatter(test_data['precipitation_sum'], predictions,s=50, alpha=0.8, color='blue')
plt.plot([0,40],[0,40],'--')
plt.xlabel('Actual Precipitation (mm)')
plt.ylabel('Predicted Precipitation (mm)')
plt.title('Actual vs Predicted Rainfall in Bangalore for the past 3 years')
plt.show()

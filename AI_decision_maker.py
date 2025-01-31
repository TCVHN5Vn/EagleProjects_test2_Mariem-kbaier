import numpy as np  # Import NumPy for numerical operations
from sklearn.tree import DecisionTreeClassifier  # Import DecisionTreeClassifier
"""
    Determines the robot's route based on the current weather using AI.


    Parameters:
    weather (str): The current weather condition ('sunny' or 'rainy').


    Returns:
    str: The chosen route ('Main Route' or 'Alternative Route').
    Weather condition mapped to route decision:
            # 0 = sunny, 1 = rainy
            # 0 = Main Route, 1 = Alternative Route
"""
def robot_route_decision(weather):


    # Training Data
    X = np.array([[0], [1], [0], [1], [0], [0], [1], [1], [0], [1]])  
    y = np.array([0, 1, 0, 1, 0, 0, 1, 1, 0, 1])


    # Train the Decision Tree model
    model = DecisionTreeClassifier()
    model.fit(X, y)


    # Convert input weather to numerical form: 'sunny' -> 0, 'rainy' -> 1
    weather_code = 0 if weather.lower() == "sunny" else 1 if weather.lower() == "rainy" else None


    # input should be either 'rainy' or 'rainy'
    if weather_code is None:
        return "Invalid weather condition! Please enter 'sunny' or 'rainy'."


    # Predict the route using AI model
    prediction = model.predict([[weather_code]])[0]
   
    # Convert prediction back to human-readable format
    return "Main Route" if prediction == 0 else "Alternative Route"


# Example Usage:
while True:
    weather_condition = input("Enter the current weather (sunny/rainy): ").strip().lower()
   
    if weather_condition in ['sunny', 'rainy']:
        break
    else:
        print("Invalid input! Please enter either 'sunny' or 'rainy'.")


print(f"Robot's Decision: {robot_route_decision(weather_condition)}")



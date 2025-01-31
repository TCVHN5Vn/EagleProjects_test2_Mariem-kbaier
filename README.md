# Trip Duration, Route Comparison, and Robot Simulation Systems

## Overview
This repository contains a series of programs developed in **C++** and **Python** for calculating trip durations, comparing routes, simulating robot movement, and using AI to predict optimal routes. The programs ensure that user inputs are valid (positive values where appropriate) and provide continuous feedback and corrections until valid data is entered. These systems are designed to demonstrate basic user input handling, mathematical calculations, and machine learning integration.

## Features

### 1. Trip Duration Calculation (Python)
   - **Functionality**: Calculates the trip duration based on distance and average speed.
   - **Validation**: Continuously asks for valid inputs if either the distance or speed is non-positive.
   - **Behavior**: Displays the estimated trip duration with two decimal precision.

### 2. AI-Powered Route Decision (Python)
   - **Functionality**: Uses a Decision Tree model to predict the best route based on weather conditions.
   - **Validation**: Continuously prompts the user for valid weather input (either "sunny" or "rainy").
   - **Behavior**: Predicts the optimal route (Main Route for sunny, Alternative Route for rainy).

### 3. Total Trip Distance Calculation (Python)
   - **Functionality**: Continuously asks for distances and calculates the total trip distance.
   - **Validation**: Ensures all distances entered are non-negative.
   - **Behavior**: Returns the total distance once all inputs are valid.

### 4. Trip Duration Calculation (C++)
   - **Functionality**: Calculates the trip duration by dividing the distance by the speed.
   - **Validation**: Ensures both the distance and speed are positive values.
   - **Behavior**: Prompts the user to re-enter values if invalid (non-positive) inputs are provided.

### 5. Route Comparison (C++)
   - **Functionality**: Compares two routes' distances and determines the shortest one.
   - **Validation**: Ensures both route distances are positive values.
   - **Behavior**: Displays the shortest route or indicates if both routes have the same distance.

### 6. Robot Movement Simulation (C++)
   - **Functionality**: Simulates robot movement in a straight line based on user input for steps and direction.
   - **Validation**: Ensures the number of steps is positive and the direction is either forward (1) or backward (-1).
   - **Behavior**: Updates and displays the robot's position at each step.

## Technologies Used
- **C++**: Used for real-time computations and simulations.
- **Python**: Used for trip duration calculations, AI-based predictions, and total distance calculation.
- **Scikit-learn (Python)**: Implements the Decision Tree Classifier for route prediction.


#include <iostream>


using namespace std;


void moveRobot() {
    int steps, direction, position = 0;


    // Get a valid number of steps
    do {
        cout << "Input the number of steps (positive number): ";
        cin >> steps;
        if (steps <= 0) {
            cout << "Error: The number of steps must be a positive number." << endl;
        }
    } while (steps <= 0);


    // Get a valid direction
    do {
        cout << "Input direction (1 = forward, -1 = backward): ";
        cin >> direction;
        if (direction != 1 && direction != -1) {
            cout << "Error: Direction should be either 1 (forward) or -1 (backward)." << endl;
        }
    } while (direction != 1 && direction != -1);


    // Move the robot and print the current position at each step
    for (int i = 0; i < steps; i++) {
        position += direction;
        cout << "Current position: " << position << endl;
    }


    // Final message
    cout << "The robot has reached its destination." << endl;
}


// Main function to call moveRobot()
int main() {
    moveRobot();
    return 0;
}

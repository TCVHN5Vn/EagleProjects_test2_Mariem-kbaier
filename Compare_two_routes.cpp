#include <iostream>
using namespace std;


int main() {
    double distance, speed;


    // Keep asking for distance and speed until both are positive
    do {
        cout << "Enter the distance of the trip (in kilometers): ";
        cin >> distance;


        cout << "Enter the speed of travel (in kilometers per hour): ";
        cin >> speed;


        // Check if either speed or distance is non-positive
        if (distance <= 0 || speed <= 0) {
            cout << "Error: Both speed and distance must be positive numbers greater than 0." << endl;
        }
        else {
            // If valid input is provided, calculate the time and display it
            double time = distance / speed;
            cout << "The total trip duration is: " << time << " hours." << endl;
        }


    } while (distance <= 0 || speed <= 0); // Keep asking until both inputs are valid


    return 0;
}

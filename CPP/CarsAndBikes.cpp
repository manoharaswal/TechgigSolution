/* Read input from STDIN. Print your output to STDOUT*/
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
#include <iostream>

using namespace std;

class Vehicle
{
	public:
		void display(){
			cout << "This is a Vehicle";
		}
};

class Car : public Vehicle
{
	public:
		void display(){
			cout << "This is a Car";
		}
};

class Bike : public Vehicle
{
	public:
		void display(){
			cout << "This is a Bike";
		}
};

int main(int argc, char *a[])
{
	int N;
	cin >> N;
	if ( N == 2 ) {
		Bike BikeObj;
		BikeObj.display();
	} else if ( N == 4 ) {
		Car CarObj;
		CarObj.display();
	} else {
		Vehicle VehicleObj;
		VehicleObj.display();
	}
	return 0;
}

/* Read input from STDIN. Print your output to STDOUT*/
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *a[])
{
	auto N = 0;
	auto EvenSum = 0;
	auto OddSum = 0;
	vector <int> arr;
	cin >> N;
	for(auto i =0; i < N;i++)
	{
		auto num = 0;
		cin >> num;
		arr.push_back(num);
		if(arr[i]%2 == 0)
			EvenSum += arr[i];
		else
			OddSum += arr[i];
	}
	if(EvenSum == OddSum)
		cout << "Tied";
	else if(EvenSum > OddSum)
		cout << "Even";
	else
		cout << "Odd";
	return 0;
}

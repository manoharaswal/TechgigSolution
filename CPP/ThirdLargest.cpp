/* Read input from STDIN. Print your output to STDOUT*/
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
#include <vector>
#include <iostream>
#include <bits/stdc++.h> 

using namespace std;

int main(int argc, char *a[])
{
	auto N = 0;
	vector<int> arr;
	cin >> N;

	for(auto i = 0;i < N; i++)
	{
		auto num = 0;
		cin >> num;
		arr.push_back(num);
	}
	sort(arr.begin(),arr.end(),greater<int>());
	cout << arr[2];
}

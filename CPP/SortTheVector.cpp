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
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char *a[])
{
	auto N = 0;
	vector <int> v;
	cin >> N;
	while ( N-- ) {
		auto n = 0;
		cin >> n;
		v.push_back(n);
	}
	sort(v.begin(), v.end(), greater<int>()); 
	for (auto i = 0; i < v.size();i++) {
		if ( i < v.size() - 1)
			cout << v[i] << " ";
		else
			cout << v[i];
	}
}

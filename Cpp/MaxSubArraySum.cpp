#include<iostream>
#include<stdio.h>
#include<climits>

using namespace std;

int MaxSubArraySum(int a[], int size)
{
	int MaxSum = 0, MaxEnd = 0;

	for (int i = 0; i < size; i++)
	{
		MaxEnd = MaxEnd + a[i];
		if (MaxSum < MaxEnd)
			MaxSum = MaxEnd;

		if (MaxEnd < 0)
			MaxEnd = 0;
	}
	return MaxSum;
}

int main()
{
	int ArrayLen,Array[10010],i;
	scanf("%d",&ArrayLen);

	for(i = 0;i < ArrayLen;i++){
		scanf("%d",&Array[i]);
	}
	int max_sum = MaxSubArraySum(Array,ArrayLen);
	cout << endl <<  max_sum << endl;
	return 0;
}

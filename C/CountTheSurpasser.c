/* Read input from STDIN. Print your output to STDOUT*/
#include<stdio.h>
int main(int argc, char *a[])
{
	int N,i,c,j;
	scanf("%d",&N);
	int arr[N];
	for(i = 0;i < N;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(i = 0;i < N;i++)
	{	
		c = 0;
		for(j = i + 1;j < N;j++){
			if(arr[i] < arr[j])
				c++;
		}
		(i == N - 1)?printf("%d\n",c):printf("%d ",c);
	}
	return 0;
}


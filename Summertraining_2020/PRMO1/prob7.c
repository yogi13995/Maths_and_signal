#include<stdio.h>

int main()
{
	int s,n=20,d=1,a =1;
	//It is a ap series so for calculatig the sum of the n numbers.
	s = (n*(2*a + (n-1)*d))/2;
	printf("sum = %d",s);
	return 0;
}

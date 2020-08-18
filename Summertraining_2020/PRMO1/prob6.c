#include<stdio.h>

int main()
{
	int a,b,x,diff;
	x = 0;
	diff = 0;
	int count = 0;
	while(diff<2)//when the difference increase 2 there is no chance of having a=b.
	{
		a = x/5;
		b = x/7;
		//printf("%d %d",a,b);
		if(a == b)
		{
			count++;
		}
		x++;
		diff = a-b;
	}
	printf("No of times = %d.",count);
	return 0;
}
	
		

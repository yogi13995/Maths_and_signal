#include<stdio.h>
#include<math.h>
int factorial(int x);
int combination(int n, int r);

int main()
{
	float p;
    //No of ways to distributr the postcards to the wrong address.
    
    p = ((combination(5,2))*(combination(2,1)));
    
    printf("No of ways = %f",p);
	return 0;
}

int factorial(int x)
{
	if(x ==1)
	{
		return 1;
	}
	
	else
	{
		return x*(factorial(x-1));
		
	}
}

int combination(int n,int r)
{
	int c ;
	  
	  c = (factorial(n)/(factorial(r)*factorial(n-r)));
	  return c;
}

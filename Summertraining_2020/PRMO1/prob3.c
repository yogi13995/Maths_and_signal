#include<stdio.h>
#include<math.h>
int main()
{
	int M1,M2,R1,R2,C1;
	float C2;
	//From equation 1 and 2 we get  quadratric equation of 'M'so the roots of the equation can be derrived as follows.
	
	int a1 =1,b1 = -46,c1 = 240;
	
	M1 = (-b1 - sqrt(b1*b1 - 4*a1*c1))/(2*a1);
	M2 = (-b1 + sqrt(b1*b1 - 4*a1*c1))/(2*a1);
	
	//From equation 1 and 3 we get  quadratric equation of 'M'so the roots of the equation can be derrived as follows.
	
	int a2 =1,b2 = -64,c2 = 240;
	
	R1 = (-b2 - sqrt(b2*b2 - 4*a2*c2))/(2*a2);
	R2 = (-b2 + sqrt(b2*b2 - 4*a2*c2))/(2*a2);
	
	C1 = 240/(M1*R1);
	C2 = 240.00/(M2*R2);
	
	printf("M = %d,%d\n",M1,M2);
	printf("R = %d,%d\n",R1,R2);
	printf("C1 = %d\n",C1);
	printf("C2 = %f\n",C2);
	
	return 0;
}

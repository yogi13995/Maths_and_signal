#include<stdio.h>

int main()
{
	int xy = 10,xz = 3,yz1,yz2;
	//there are two cases of the points to be on a straight line which satisfy the given conditions and those are XZY and ZXY.
	
	//For XZY
	yz1 = xy - xz;
	//for ZXY
	yz2 = xy + xz;
	
	printf("multiplicaton = %d\n",yz1*yz2);
	return 0;
}

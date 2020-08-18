#include<stdio.h>
#include<math.h>

int main()
{
	int n;
    //there are three cases of having two different balls.
    //red and blue,red and green,blue and green
    //After simplfying the equation we get 
    n = sqrt((299+1)/3);  
    printf("n = %d",n);
	return 0;
}



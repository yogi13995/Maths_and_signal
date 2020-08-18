#include<stdio.h>
#include<math.h>

int main()
{
int i,j,a,b,c;
float ar,area;
area =0;
for(i=1;i<4;i++)
	{
		a = i;
		for(j=1;j<4;j++)
		{
			b = j;
			if((a + b)>3)
			{
				c = 7 -(a+b);
				printf("a = %d ,b = %d ,c = %d\n",a,b,c);
				ar =  sqrt(3.5*  (3.5-a) * (3.5-b) * (3.5-c));
				printf("area = %f\n",ar);
				
			}
			else
			{
			break;
			}
			if(area<ar)
			{
				area = ar;
			}
		}
	}
	printf("max area = %f\n.",area);
	return 0;
}
		

#include <stdio.h>
int main()
{
	int number1,number2,result;
	printf("Enter those numbe:");
	scanf("%d",&number1,&number2);
	result=sum(number1,number2);
	printf("The sum of those number is %d",result);
	return (0);
}
int sum(int number2,int number1)
{
 int number3;
 number3=number1+number2;
 return(number3)
}


#include<stdio.h>
int answer(int x)
{
     int result;
     result=x %2;
     return(result);
}
int main()
{
     int x,result;
     printf("Enter a number:");
     scanf("%d",&x);
     result=answer(x);


     if (result=0)
          {
               printf("it is odd");
          }
          else 
               printf("it is even");
                   return 0;
}

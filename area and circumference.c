#include <stdio.h>

int area(int r)
{
    int area;
    area=22/7*(r*r);
    return area;
}
int circumference(int r)
{
    
    int c=2*(22/7)*r*r;
    return c;
}
int main() 
{
    int radious,answer,choice;
    printf("Enter the radious:");
    scanf("%d",&radious);
    printf("Enter 1 for area\n");
    printf("Enter 2 for circumference\n");
    printf("Enter you choice:");
scanf("%d",&choice);
switch(choice)
    {
        case 1:
        {
        answer=area(radious);
        printf("The area is:%d",answer);
        break;
        }
    
    
        case 2:
        {
            answer=circumference(radious);
            break;
        }
    }
    
    

    
    return 0;
}
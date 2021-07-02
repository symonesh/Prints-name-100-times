#include <stdio.h>

int main() {

    int x,y,z=1;
    printf("Enter the number:");
    scanf("%d",&x);
    for (y=1;y<=x;y++)
    z=z*y;
printf("The factorial is:%d",z);
return 0 ;
}


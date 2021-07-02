#include <stdio.h>  
   
int main() {  
    int x,y; 
    printf("10 odd numbers from 1\n");  
    for(x = 1; y <= 10  ; x++) {  
        if(x%2 != 0) { 
           printf("%d,", x);
           y+=1;
        }  
    }  
   
    return 0;  
} 

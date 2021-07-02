#include <stdio.h>  
   
int main() {  
    int x; 
    printf("Even numbers between 1 to 100\n");  
    for(x = 1; x <= 100; x++) {  
        if(x%2 == 0) { 
           printf("%d\n", x);  
        }  
    }  
   
    return 0;  
} 

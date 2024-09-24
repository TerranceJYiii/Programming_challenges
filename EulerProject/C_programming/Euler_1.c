#include <stdio.h>

int Euler_1 (int num){
    
    int ans = 0;

    for (int i = 0; i < num; i++){
        
        if (i % 3 == 0 || i % 5 == 0){
            
            ans += i;

        } 
    }

    return ans;
}

int main (void){
    
    int answer = Euler_1(1000);
    printf("Answer for Project Euler 1 is %d", answer);
    return 0;
}
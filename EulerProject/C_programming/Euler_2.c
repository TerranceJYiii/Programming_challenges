#include <stdio.h>
#include <stdbool.h>

int Euler_2 (int maxValue){
    int ans = 2;
    bool change_A = false;
    int a = 1;
    int b = 2;

    while (a < maxValue && b < maxValue){
        change_A = !change_A;

        if (change_A){
            a = a + b;
            if (a % 2 == 0){
                ans += a;
            }
        }
        else{
            b = a + b;
            if (b % 2 == 0){
                ans += b;
            }
        }
    }

    return ans;

}

int main (void){
    int answer = Euler_2(4000000);
    printf("Answer for Project Euler 2 is %d", answer);
    return 0;
}
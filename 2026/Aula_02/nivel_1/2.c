#include <stdio.h>

int main() {

  float TC = 0, TF= 0, TK= 0;

    printf("Digite a temperatura em Celsius: ");
    scanf("%f", &TC);
    TF=TC * 1.8 + 32;
    TK= TC + 273.15; 
    printf("A temperatura em Fahrenheit :%.1f\n", TF);
    printf("A temperatura em Kelvin : %.1f\n", TK);
 

    return 0;
}
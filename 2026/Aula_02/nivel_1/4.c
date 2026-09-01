#include <stdio.h>

int main() {

  int total = 0, num1, num2, num3;
  float media = 0;

    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);
    printf("Digite o segundo numero: ");
    scanf("%d", &num2);
    printf("Digite o terceiro numero: ");
    scanf("%d", &num3);


    if (num1 > num2 && num1 > num3) {
        printf("o maior numero e: %d", num1);
    } else if (media < 5 ){
        printf("Reprovado  a nota e: %.1f\n", media);
    }
    else {
        printf("Recuperacao a nota e:  %.1f\n", media);
    }

    return 0;
}
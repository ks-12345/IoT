#include <stdio.h>

int main() {

  int total = 0, num1, num2, num3, num4;
  float media = 0;

    printf("Digite o primeiro nota: ");
    scanf("%d", &num1);
    printf("Digite o segundo nota: ");
    scanf("%d", &num2);
    printf("Digite o terceiro nota: ");
    scanf("%d", &num3);
    printf("Digite o quarta nota: ");
    scanf("%d", &num4);
    total = num1 + num2 + num3 + num4;
    media = total / 4;

    if (media >= 7) {
        printf("Aprovado a nota e: %.1f\n", media);
    } else if (media < 5 ){
        printf("Reprovado  a nota e: %.1f\n", media);
    }
    else {
        printf("Recuperacao a nota e:  %.1f\n", media);
    }

    return 0;
}
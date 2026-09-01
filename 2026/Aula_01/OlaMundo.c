#include <stdio.h>

int main() {

    int idade = 0, ano_nasc = 0, num1, num2, num3;

    printf("Ola mundo!\n");
    printf("Digite sua idade: ");
    scanf("%d", &idade);
    ano_nasc = 2026 - idade;
    printf("Voce nasceu em %d\n", ano_nasc);


    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);
    printf("Digite o segundo numero: ");
    scanf("%d", &num2);
    printf("Digite o terceiro numero: ");
    scanf("%d", &num3);
    printf("A soma de %d, %d e %d é %d\n", num1, num2, num3, num1 + num2 + num3);

    return 0;
}
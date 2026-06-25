#include <stdio.h>


int mostrar_linea()
{
    printf("----------------------------------------\n");

    return 0;
}





int main()
{

    int i;
    int numero;
    int suma;
    int factorial;


    printf("\n");
    printf("========================================\n");
    printf("       BIENVENIDO A SPANISH C            \n");
    printf("========================================\n");
    printf("\n");



    printf("Iniciando pruebas...\n");
    printf("\n");



    mostrar_linea();



    printf("PRUEBA 1: Variables\n");

    numero = 10;
    suma = 0;


    printf(
        "Numero guardado: %d\n",
        numero
    );


    printf(
        "Suma inicial: %d\n",
        suma
    );



    mostrar_linea();





    printf("PRUEBA 2: Bucle para\n");


    for(i = 1; i <= 10; i = i + 1)
    {

        suma = suma + i;


        printf(
            "Iteracion %d -> suma = %d\n",
            i,
            suma
        );

    }



    printf(
        "Suma final: %d\n",
        suma
    );



    mostrar_linea();







    printf("PRUEBA 3: Condiciones\n");


    if(suma > 50)
    {

        printf(
            "La suma es mayor que 50\n"
        );

    }

    else
    {

        printf(
            "La suma es menor o igual que 50\n"
        );

    }





    if(numero == 10)
    {

        printf(
            "Numero correcto\n"
        );

    }

    else
    {

        printf(
            "Numero incorrecto\n"
        );

    }



    mostrar_linea();







    printf("PRUEBA 4: Mientras\n");


    numero = 5;


    while(numero > 0)
    {

        printf(
            "Cuenta regresiva: %d\n",
            numero
        );


        numero = numero - 1;

    }


    printf(
        "Despegue!\n"
    );



    mostrar_linea();









    printf("PRUEBA 5: Factorial\n");


    numero = 6;
    factorial = 1;


    while(numero > 1)
    {

        factorial = factorial * numero;


        printf(
            "Multiplicando por %d, resultado %d\n",
            numero,
            factorial
        );


        numero = numero - 1;

    }



    printf(
        "Factorial final: %d\n",
        factorial
    );



    mostrar_linea();








    printf("PRUEBA 6: Tabla del 5\n");


    for(i = 1; i <= 10; i = i + 1)
    {

        printf(
            "5 x %d = %d\n",
            i,
            5 * i
        );

    }



    mostrar_linea();








    printf("PRUEBA 7: Muchas cadenas\n");


    printf("Hola mundo!\n");
    printf("Esto fue escrito en SpanishC\n");
    printf("Traducido automaticamente a C\n");
    printf("Compilado usando GCC\n");



    mostrar_linea();








    printf("PRUEBA 8: Valores pares\n");


    for(i = 0; i <= 20; i = i + 1)
    {

        if(i % 2 == 0)
        {

            printf(
                "%d es par\n",
                i
            );

        }

    }




    mostrar_linea();







    printf("PRUEBA 9: Final\n");


    printf(
        "Todas las pruebas terminaron correctamente!\n"
    );


    printf(
        "SpanishC funciona :)\n"
    );


    printf("\n");
    printf("========================================\n");


    return 0;
}
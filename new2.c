#include <stdio.h>

int main()
{
    printf("this program adds to numbers.");
    int a;
    int b;
    int result;
    printf("enter a: ");
    scanf("%d",&a);
    printf("enter b: ");
    scanf("%d",&b);

    result = a + b;
    printf("\nsum of a and b is: ",result);
    return 0;
}
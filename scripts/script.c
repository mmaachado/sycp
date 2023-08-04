#include <stdio.h>


int main() {

    char target[100]; 
    int door;

    printf("Type the target:\n"); 
    scanf("%s", &target);

    printf("Type the door:\n"); 
    scanf("%i", &door);

    printf("Starting attack on target %s, in door %i", target, door);

    return 0;
}
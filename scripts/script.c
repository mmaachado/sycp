#include <stdio.h>
#include <string.h>

int main() {

    char target[100]; 
    char response[3];
    int door;

    printf("Type the target:\n"); 
    scanf("%s", &target);

    printf("Type the door:\n"); 
    scanf("%i", &door);

    printf("Do you confirm the attack on: %s\n", target);
    scanf("%s", response);

    if (strcmp(response, "y") == 0) {
        printf("Starting attack on target %s, using door %i", target, door);
    } else {
        printf("Stopping attack. . .");
    }

    return 0;
}
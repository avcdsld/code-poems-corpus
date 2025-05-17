#include <stdio.h>
#define LIFESPAN 81

int main () {

int age= 0;
int death = 0;
int life = 1;

while (! death) {
    age++;
    sleep(31556926);
    if (age == LIFESPAN) death = life;
}

}

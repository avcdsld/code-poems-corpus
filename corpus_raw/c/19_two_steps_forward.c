#include <stdbool.h>

int main(int argc, const char *argv[]) {
    int x = 1;
    while (true) {
        x = x << 2;
        x = x >> 1;
    }

    return 0;
}

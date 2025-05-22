#include <stdio.h>

unsigned int n = 1701998444;

int main()
{
    int i = 0;

    while(i < n) {
        putc(((n >> (i % 4) * 8) & 0xff) +
              4 * ((int) (i % 8 % 7) / 6),
              stdout);
        i++;
    }

    return n;
}

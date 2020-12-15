#include <stdio.h>
#include <stdint.h>

uint32_t content[] = {2,0,6,12,1,3};
uint32_t spoken[30000000] = {0};

int main(int argc, char *argv[])
{

    uint32_t new_spoken = 0;
    uint32_t turn = 1;
    uint32_t last_turn = 0;

    for(int i = 0; i<sizeof(content)/sizeof(uint32_t); i++, turn++)
        spoken[content[i]] = turn;

    for(;turn <= 30000000; turn++)
    {
        if(!last_turn)
            new_spoken = 0;
        else
            new_spoken = turn - 1 - last_turn;

        last_turn = spoken[new_spoken];
        spoken[new_spoken] = turn;
    }

    printf("%d\n", new_spoken);

    return 0;
}

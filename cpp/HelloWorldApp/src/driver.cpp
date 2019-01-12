#include <iostream>
#include <driver.h>
#include <Randomize/randomize_util.h>


void RandomNumberGenerator::generate(int num)
{
    if (_chance > 0)
    {
        if (getRandom() == num)
        {
            puts("Nice one");
        }
        else
        {
            puts("Nope");
        }
        _chance--;
    }
    else
    {
        puts("Out of goes mate, apologies");
    }
};


#include <iostream>
#include <driver.h>
#include <Randomize/randomize_util.h>

RandomNumberGenerator::RandomNumberGenerator(int chance)
{
    this->chance = chance;
};

void RandomNumberGenerator::generate(int num)
{
    if (this->chance > 0)
    {
        if (getRandom() == num)
        {
            std::cout << "Nice one" << std::endl;
        }
        else
        {
            std::cout << "Nope" << std::endl;
        }
        this->chance--;
    }
    else
    {
        std::cout << "Out of goes mate, apologies" << std::endl;
    }
};

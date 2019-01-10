#pragma once

#include <driver.h>

class RandomNumberGeneratorInterface
{
    private:
        RandomNumberGenerator *attempt;

    public:
        RandomNumberGeneratorInterface(int length);
        void start(int num);
};

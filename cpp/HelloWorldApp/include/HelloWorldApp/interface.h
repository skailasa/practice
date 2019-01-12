#pragma once

#include <driver.h>

class RandomNumberGeneratorInterface
{
    private:
        RandomNumberGenerator *attempt;
        int _length;       

    public:
        RandomNumberGeneratorInterface(int length); 
        void start(int num);
};

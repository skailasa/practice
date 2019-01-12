#pragma once
#include <string>
#include <iostream>
using namespace std;

class RandomNumberGenerator
{
    private:
        int _chance;
    public:
        RandomNumberGenerator(int chance): _chance(chance) {};
        void generate(int num);
};

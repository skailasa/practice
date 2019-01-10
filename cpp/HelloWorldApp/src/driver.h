#pragma once

class RandomNumberGenerator
{
    private:
        int chance;
    public:
        RandomNumberGenerator(int chance);
        void generate(int num);
};

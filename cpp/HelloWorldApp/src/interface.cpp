#include <driver.h>
#include <HelloWorldApp/interface.h>

void RandomNumberGeneratorInterface::start(int num)
{
    this->attempt->generate(num);
}

RandomNumberGeneratorInterface::RandomNumberGeneratorInterface(int length)
{
    this->attempt = new RandomNumberGenerator(length);
}

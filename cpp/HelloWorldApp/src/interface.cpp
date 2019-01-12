#include <driver.h>
#include <HelloWorldApp/interface.h>

RandomNumberGeneratorInterface::RandomNumberGeneratorInterface(int length): _length(length)
{
    // new returns a pointer to a random number generator object
    attempt = new RandomNumberGenerator(_length);
}

void RandomNumberGeneratorInterface::start(int num)
{   
    // arrow operator allows you to access members of a struct/class
    // through a pointer
    attempt -> generate(num);
}

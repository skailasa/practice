#include <HelloWorldApp/interface.h>

int main ()
{
    RandomNumberGeneratorInterface g(3);
    g.start(0);
    return 0;
}

#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

const string clone_prefix = "clone-";
const string unk = "unknown";

class Person
{
    private:
        int _age=0;
        string _forename = unk;
        string _surname = unk;
    public:
        Person(); // default constructor
        Person(const string & forename, const string & surname, const int & age);
        Person(const Person &); // copy constructor
        ~Person(); // destructor
        void print() const;
};

Person::Person() {
    puts("The default constructor");
}

Person::Person(const string & forename, const string & surname, const int & age)
: _forename(forename), _surname(surname), _age(age) {
    puts("constructor with arguments");
}

Person::Person(const Person & a)  {
    puts("copy constructor");
    _forename = clone_prefix + a._forename;
    _surname = clone_prefix + a._surname;
    _age = a._age;
}

Person::~Person() {
    puts("destructor");
}

void Person::print() const {
    printf("This person's name is %s %s and they are %d years old\n", _forename.c_str(), _surname.c_str(), _age);
}

int main()
{   
    // Default construction, no params
    Person me;
    me.print();
    
    // Construct with params
    const Person also_me("Srinath", "Kailasa", 24);
    also_me.print();
    
    // Clone a Person object
    const Person clone = also_me;
    clone.print();
    
    return 0;
}

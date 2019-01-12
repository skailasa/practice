#include <cstdio>
#include <iostream>
using namespace std;

class Rational {
    int _n = 0; //numerator
    int _d = 1; // denominator

public:
    // default constructor
    Rational(int numerator = 0, int denominator = 1): _n(numerator), _d(denominator) {};
    // copy constructor
    Rational(const Rational & rhs): _n(rhs._n), _d(rhs._d) {};
    // destructor
    ~Rational();
    int numerator() const {return _n; };
    int denominator() const {return _d; }; 
    Rational & operator = (const  Rational &);
    Rational operator + (const Rational &) const;
    Rational operator - (const Rational &) const;
};

Rational::~Rational() {
    _n = 0; _d = 1;
}

Rational & Rational::operator = (const Rational & rhs) {
    if (this != &rhs) {
        _n = rhs.numerator();
        _d = rhs.denominator();
    }
    return *this;
}

Rational Rational::operator + (const Rational & rhs) const {
    return Rational((_n * rhs._d) + (_d * rhs._n), _d * rhs._d);
}

Rational Rational::operator - (const Rational & rhs) const {
    return Rational((_n * rhs._d)-(_d * rhs._n), _d * rhs._d);
}

std::ostream & operator << (std::ostream & o, const Rational & r) {
    if (r.denominator() == 1) return o << r.numerator();
    else return o << r.numerator() << '/' << r.denominator();
}

int main() {
    Rational a = 7; // 7/1
    cout << "a is: " << a << endl;
    Rational b(5, 2);
    cout << "b is: " << b << endl;
    
    cout << a << "+" << b << " = " << a + b << endl;    

    return 0;
}

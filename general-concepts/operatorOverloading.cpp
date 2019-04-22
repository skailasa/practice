#include<iostream>
#include<string>

using namespace std;

class Complex
{
public:
    int a,b;
    void input(string s)
    {
        int v1=0;
        int i=0;
        while(s[i]!='+')
        {
            v1=v1*10+s[i]-'0';
            i++;
        }
        while(s[i]==' ' || s[i]=='+'||s[i]=='i')
        {
            i++;
        }
        int v2=0;
        while(i<s.length())
        {
            v2=v2*10+s[i]-'0';
            i++;
        }
        a=v1;
        b=v2;
    }
};

Complex operator +(const Complex& a, const Complex& b){
    Complex res;
    res.a = (a.a + b.a);
    res.b = (a.b + b.b);
    return res;
}

ostream& operator<<(ostream& os, const Complex& c) {
    return os << c.a << (c.b > 0 ? '+' : '-') << 'i' << c.b;
}

int main() {
    Complex c1;
    Complex c2;
    string s1 = "4+i2";
    string s2 = "6+i3";
    c1.input(s1);
    c2.input(s2);
    
    cout <<"c1=" << c1 << endl;
    cout << "c2=" << c2 << endl;
    cout << "c1+c2="<<c1 + c2 << endl;
    return 0;
}

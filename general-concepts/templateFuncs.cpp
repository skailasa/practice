#include <iostream> 
#include <typeinfo>

using namespace std;

template <class T> // class || typename 
T sum (T a, T b) {
	T result;
	result = a + b;
	return result;
}

template <typename T1, typename T2>
void myFunc(T1 a, T2 b) {
	cout << "a is : " << a << endl;
	cout << "b is: " << b << endl;
}

template <typename T>
void f(T x) {
	cout << typeid(T).name() << " " << x << '\n';
}


int main () { 
	int i=5, j=6;
	double f=5.0, g=6.0;
	cout << sum<int>(i,j) << endl; 
	cout << sum<double>(f,g) << endl;
	cout << myFunc<int, double>(i, g) << endl;
	cout << f<char>('a') << endl;
	cout << f<int>(1) << endl;
	return 0;
}
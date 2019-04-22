#include <iostream>

using namespace std;

template <typename T>
class MyPair {
private:
	T mVals[2]
public:
	T GetMax() const;
}

template <typename T>
MyPair<T>::MyPair(const T& first, const T& second) {
	mVals[0] = first;
	mVals[1] = second;
}

template <typename T>
MyPair<T>::GetMax() const {
	if(this->m_values[0] > this->m_values[1])
		return m_values[0];
	else
		return m_values[1];
}


int main(int argc, char** argv) {
	MyPair<int> a(1,2);
	MyPair<char> b('a', 'b');
	cout << "Max is: " << a.getMax() << endl;
	cout << "Max is: " << b.getMax() << endl; 
}
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

int main (int argc, char* argv) {
	// Model ownership with shared pointer, no copy/assignment operators
	std::unique_ptr<MyPair> pair(new MyPair(1, 2));
	cout << pair.GetMax();

	// Need move semantics to reassign
	std::unique_ptr<MyPair> pair2;
	pair2 = std::move(pair);

	// Cant pass by reference, can't reassign -> like singleton
}
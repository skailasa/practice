#include <iostream>
#include <string>

using namespace std;

template <typename T>
class stack {
private:
    static const int defaultsize = 10;
    static const int maxsize = 1000;
    int _size;
    int _top;
    T * _stkptr;

public:
    // keyword disallows implicit type conversions for methods on this object
    explicit stack(int s = defaultsize);
    ~stack() { delete[] _stkptr; }
    T & push( const T &);
    T  & pop();
    bool isempty() const { return _top < 0; }
    bool isfull() const { return _top >= _size -1; }
    int top() const {return _top;}
    int size() const {return _size;}
};

// stack<T> constructor
template <typename T>
stack<T>::stack(int s) {
    _size = s;
    _stkptr = new T[_size];
    _top = -1;
}

template <typename T>
T & stack<T>::push (const T & i) {
    return _stkptr[++_top] = i;
}

template <typename T>
T & stack<T>::pop () {
    return _stkptr[_top--];
}

int main() {
    // create an integer stack of size 5
    stack<int> s(5);
    cout << "size of s: " << s.size() << endl;
    cout << "s top: " << s.top() << endl;
    
    int array[] = {1, 2, 3, 4};

    for (int i: array) {
        s.push(i);
    }

    cout << "after pushes, top: " << s.top() << endl;
    
    return 0;
}

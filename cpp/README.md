# C++

[notes from learn c++.com](https://www.learncpp.com/cpp-tutorial/25-floating-point-numbers/)

## 1. Introduction

## 2. Variables and Fundamental Data Types

A given variable may use a number of bytes, with the amount depending on type.
You may need to keep track of this for the dreaded case of int overflow etc.

2 bits can hold 4 possible values:

| bit 0 | bit 1 |
|-------|-------|
|0      | 0     |
| 1     | 0     |
| 0     | 1     |
| 1     | 1     |


And n bits can therefore hold 2^n values, as a byte is 8 bits - it can store
2^8 (256) values.

Get's important when a program has a massive number of variables. Surprisingly,
the size of a given type is compiler/architecture dependent.

However C++ guarantees a minimum sie for basic types

category | type | min size | note
bool | bool | 1 byte |
character | char | 1 byte |  may be signed or unsigned, always 1 byte
 | wchar\_t | 1 byte | 
 | char16\_t | 2 bytes | C++11
 | char32\_t | 4 bytes | C++11
integer | short | 2 bytes |
 | int | 2 bytes |
 | long | 4 bytes |
| long long | 8 bytes |
floating point | float | 4 bytes |
 | double | 8 bytes |
 | long double | 8 bytes |


size | number range
1 byte signed | -128 to 128
1 byte unsigned | 0 to 255
2 bytes unsigned | 0 to (2^16-1)
2 bytes signed | -32768 to 32768



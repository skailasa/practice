# Hello World C++ App

This directory is a sample project structure for C++ development. 

This is basiclaly a library which can be used directly, or could be used as a 3rd party
library by someone else.

The key idea is separating the public header files from the private ones. I.e. we
need to have some control over which functions people can invoke, and private functions
- an interface if you will.


## Project Structure

```bash
HelloWorldApp
+
+->CMakeLists.txt
|->README.md
+->include
| +->HelloWorldApp
|    +->publicheader(s).h
+->src
| +->privateheader(s).h
| +->code(s).cpp
|
+->libs
| +->3rdPartyLibs
|
+->tests
```

### `include/`

By convention usually for header files, and the modern pattern is to place header
files here that you intend to expose publicly. The placement of another directory
in here with the same name as your project forces a user to write:

```c++
#include <HelloWorldApp/public_header.sh>
```

instead of:

```c++
#include <public_header.sh>
```

which makes it a lot more obvious where they are calling in code from. 

### `src/`

As usual contains source code, as well as private header files for internal use. All
of the lib's code goes here.

### `libs/`

This consists of **third party libraries** that are needed by this project. Noting that
there are two ways of using third party software in C++, (static and dynamic) this directory
is *only* for static libraries.

### `tests/`

As usual, kept separate from source code

### `CMakeLists.txt`

This is a config file 

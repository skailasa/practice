cmake_minimum_required( VERSION 3.0 )

project(HelloWorldApp)

# flags

# include files
include_directories(./include ./src ./libs/Randomize/include)

# target
add_executable(binary ./src/main.cpp ./src/driver.cpp ./src/interface.cpp)

# 3rd party libs

## I've already compiled this library to pretend that it's really 3rd party
add_library(randomize STATIC IMPORTED)
set_property(TARGET randomize PROPERTY IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/libs/Randomize/lib_randomize.a)
target_link_libraries(binary randomize)


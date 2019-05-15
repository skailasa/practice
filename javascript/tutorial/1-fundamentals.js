"use strict";

/*
Vars
*/

// Variable declarations
let x;

// Assign data
x = 'Hello World';

// Print to console
console.log(x);


// $ and _ are valid var names in JS
let $ = 10;
let _ = 11;

console.log( $ + _);

// keywords rejected as variable names by compiler

// Like C, has const
const YEAR = 2019;

console.log("Current Year: ", YEAR);

/*
Simple Types
*/

// Number type, covers ints and floats
let n = 123;
n = 1.23;

console.log(n);


// 3 types of strings in JS
// Simple quotes, double and single - no differentiation
// Backticks allow the embedding of variables/expressions

let name = 'Sri';

console.log(`Hello, ${name}`);
console.log(`1 + 2 = ${1+2}`);

// Special null type, reference to non-existing object

let age = null;
console.log(age);

// Undefined values have their own type too, null is reccomended
let y;

console.log(y);

// typeof operator for type checking

console.log(typeof 1 == "number"); // true

/*
Type Conversions
 */

// JS coerces types for you a lot

// ToString
let value = true;
console.log(typeof value);

value = String(value);
console.log(typeof value);

//ToNumber
console.log("6"/"2"); // Danger

let num = Number("");
console.log(num); // Can be dodgy, this gives 0

// More coercion
console.log('1 ' + 2);

// Truthy/Falsy in JS

console.log(Boolean(1)); // True
console.log(Boolean(0)); //  False

let apples = "2";
let oranges = "3";

/*
Operators
 */

// Unary decimal conversion
console.log( +apples + +oranges); // 5

// Assignment, can chain in JS

let a, b, c;

a = b = c = 1 + 2;

// Evaluated from right to left
// Assignment operator always returns a value

/*
Conditionals
 */

// If is C like
let year = 2019;

if (year == 2019) {
    console.log("year is", year);
}

// JS has ternary conditional operators
let res = 1 == 1 ? "that's right" : "what";

console.log(res);

/*
Loops
 */

// Very similar to C in syntax

let i = 0;
while (i < 2) {
    console.log(i);
    i++;
}

// Have some sugar for this when you want something to
// be followed by a loop

let j = 0;
do {
    console.log(j);
    j++;
} while (j < 3);

/*
Switch
 */

x = '1';

switch(x) {
    case '1': // if (x == '1')
        console.log('srinath');
    break;
    case '2':
        console.log('kailasa');
        break;
    default:
        console.log("srinath kailasa");
}

// If there's no break clause, execution continues
// with the next case without any checks
// Type matters in switch statements, equality check is strict


/*
Simple functions
 */

// declared with function keyword

function firstFunc() {
    console.log("Hello World");
}

// Variable name shadowing leads to preffered access of vars
// in local scope if they share a name

let glob = 'foo';

function secondFunc() {
    let glob = 'bar';
    console.log(glob);
}
secondFunc(); // bar

// Default pass by value in JS

// Default values, similar declaration to Python

function withDefault(firstname, lastname='kailasa') {
    console.log("Hello " + firstname + " "+ lastname);
}

withDefault('srinath');
withDefault('joe', 'bloggs');

// Functions are first class in JS
// Can use 'function expression' to create them too as a result

let sayHi = function() {
    console.log("hello");
};

sayHi();
console.log(sayHi);

// Can therefore deal with functions like any other value
// copy to other vars, like Python

let newHi = sayHi;
newHi();

// Function expressions only usable after declaration in code
// Function Declarations usable from anywhere in scripts
// Use function expressions to declare anonymous functions

// Arrow functions

let sum = (arg1, arg2) => arg1 + arg2;
console.log(sum(1, 2));

// parenthesis can  be omitted if only one argument
let double = n => 2*n;
console.log(double(4));

// no args
let yo = () => "Yo!";
console.log(yo());
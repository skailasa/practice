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

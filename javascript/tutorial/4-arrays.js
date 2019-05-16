/*
Arrays
 */

// Two syntaxes ...

// rarely used constructor
let arr = new Array();

// and commonly used literal
let arr2 = [];

let fruits = ["apples", "oranges", "pears"];

// can add elements to array with indexing
fruits[3] = 'sri';

console.log(fruits);

// Can store elements of any type
fruits[4] = true;

console.log(fruits);

// In JS arrays are attempted to be stored in contiguous memory
// Can have arrays with 'holes' in due to the way things can
// be inserted though, so cases exist where this optimisation
// doesn't happen

// Loops
for (let i=0; i<fruits.length; i++) {
    console.log(fruits[i]);
}

// Arrays are NOT primitives, they are objects, so can use
// for .... in syntax to loop through

for (let key in fruits) {
    console.log(fruits[key]);
}

// This iterates over all properties of the obj, in this case
// array elements.

// Note that array length is calculated from the greatest index
// number + 1, rather than the number of elements in the array


// Has list comprehension type operation
fruits.forEach((item, index, array) => {console.log(item)});

// sorting an array
let arr3 = [1, 2, 15];

arr3.sort();

console.log(arr3); // [1, 15, 2]

// strange answer, as sorted as strings by default, have to
// implement numeric comparison

function compareNum(a, b) {
    if (a > b) return 1;
    if (a == b) return 0;
    if (a < b) return -1;
}

arr3.sort(compareNum);
console.log(arr3);


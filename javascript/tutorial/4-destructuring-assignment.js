/*
JS allows python style object unpacking for objects and arrays

 Called 'destructuring assignment'
 */

// Iterable destructuring
let arr = ["a", "b"];
let [a, b] = arr;

arr[2] = 'c';

// can ignore elements
let [c, ,d] = arr;


// doesn't have to be vars on the lhs
let user = {}; // object literal
[user.name, user.surname] = "Srinath Kailasa";

// Can get the rest using following syntax
[e, f, ...rest] = arr;
console.log(rest); // array

// Object destructuring
let opts = {
    title: "menu",
    width: 100,
    height: 200
};

// let {title, width, height} = opts; // notice curly braces

// use the same variable names as properties, because order
// doesn't matter in object destructuring

// If properties are missing, can set default values to prevent
// crit fails

let {bar='foo', title, width, height} = opts;
console.log(bar);

// can unpack into custom names too
let {width: w, height: h, title: t} = opts;

// and the ..rest operator works here too
let {title1, ...rest1} = opts;

// props accessed with dot method
console.log(rest1.height);

// Allows us to write smart function parameters

let opt2 = {o1: 'a', o2: 'b'};

function test({o1 = 'a', o2 = 'b'}) {
    console.log(o1, o2);
}

// Like python kwargs dict
test(opts);

// same syntax for destructuring assignment

function test2({o1: v1 = 'a', o2: v2 = 'b'}) {
 console.log(v1, v2);
}

test2(opts);

// need to pass an arg above, but can fix this by making {}
// the default value

function test3({o1: v1 = 'a', o2: v2 = 'b'} = {}) {
    console.log(v1, v2);
}

test3();

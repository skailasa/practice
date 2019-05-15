/*
JS objects

- Can be created with curly braces
- Optional list of *properties*, k,v pairs.
    - k is a string, v can be anything
 */
const readline = require('readline');

const rl = readline.createInterface(
    {
        input: process.stdin,
        output: process.stdout
    }
);

// Object creation syntax 1
let user1 = new Object(); // Constructor
let user2 = {}; // Object literal (JSON)


let user3 = {
    name: "Srinath",
    age: 25
};

// Can dynamically add/remove properties
user3.isAdmin = true;
delete user3.age;

// Can have multiword properties

let user4 = {
    "some property": false
};

// access using different notation
// set
user4["some property"] = true;
// get
console.log(user4["some property"]);
// del
delete user4["some property"];

// computed properties
/*
Can use square brackets in object literal for computed
properties
 */


let fruit = 'apple';
let bag = {
    [fruit + 'Computers']: 5 // bag.appleComputers = 5
};

// Reserved keywords are allowed property names
let obj = {
    for: 1,
    let: 2,
    return: 3
};

// Property value shorthand
// Often use existing values as property names


function makeUser(name, age) {
    return {
        name: name,
        age: age
    };
}

let user = makeUser("Sri", 25);

// So shorthand exists to speed this up

function makeBetterUser(name, age) {
    return {
        name,
        age
    };
}

// No errors raised if a property doesn't exist ...
// Can use 'in' to check for existence, returns bool

// Fundamental difference between user defined objects
// JS primitives is that they are always copied by reference

// This effects comparison, as there is comparison by
// reference for objects, but value for primitives

// Const objects can be changed in JS
const user5 = {
    name: "Sri"
};

user5.age = 25;

/*
This works because const fixes the value of user5 to
itself, and here user5 stores the reference to the same
object at all times - so the age goes inside the object
and it's not being reassigned. Reassignment is the thing
that's not allowed in const values.
 */

// To (deep) copy an object we clone it, but rarely done
let clone = {};

// No built in for this, have to implement
for (let key in user5) {
    clone[key] = user[key];
}

// Can also use Object.assign
Object.assign(clone, user, user2);


/*
Symbol type

 - Property keys may be either of string or symbol type.
    - Not numbers, not bools
 */

// Symbol value represents a unique identifier
let id = Symbol(description='id');

// symbols are guaranteed to be unique, even with same
// description - these don't effect hash

// Symbols are never coerced into strings

// Allow for the creation of hidden/private properties

let person = {name: "sri"};

let dob = Symbol('year of birth');
person[dob] = 1994;
console.log(person[dob]);

// Allows us to reuse property names, as they are
// guaranteed to be unique

// Literal symbols need square brackets
let prop = Symbol('property')

let obj2 = {
    [prop]: 123
};

// Symbols are skipped in for ... in loops, i.e. they're
// hidden. But still copied over with Object.assign

/*
Global symbols

- global symbol registry, checks for symbol - or creates
new one.
 */

// read from global registry
let pid = Symbol.for('pid'); // created if it doesn't exist

// read again
let pidAgain = Symbol.for('pid');

console.log(pid === pidAgain); // true

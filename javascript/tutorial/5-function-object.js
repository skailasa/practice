/*
Functions are objects in JS, like in Python.

Can have properties, pass by reference etc.
 */

// name property, accesses function's name
function sayHi() {
    console.log('hi');
}

console.log(sayHi.name);

// Also works for function expressions

let sayHello = function() {
    console.log('hello');
};

console.log(sayHello.name);

// length returns number of function parameters
console.log(sayHi.length);

// rest parameters are not counted.

// can add custom properties to functions
function countsCalls() {
    countsCalls.counter++;
}
countsCalls.counter = 0; // initialise

countsCalls();
countsCalls();
console.log(`called ${countsCalls.counter} times`);


// can rewrite the above making use of closures
function makeCounter() {
    function counter() {
        return counter.count++;
    }
    counter.count = 0;
    return counter;
}

let counter = makeCounter();
console.log(counter());
console.log(counter());

// Named function expressions
let sayYo = function func(who) {
    console.log(who);
};

/*
- Allows the function to reference itself internally
- It is not visible outside of the function

e.g. can call itself
 */

let namedFE = function func(who) {
    if (who) {
        console.log(`Hello ${who}`)
    } else {
        func("Guest");
    }
};

// Only worked in scope of function
// No such mechanism for function declaration




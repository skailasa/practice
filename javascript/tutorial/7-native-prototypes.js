/*
Prototype widely used by core JS, all built-in constructors use it.
 */

// literal construction of objects just shorthand
obj = new Object(); // same as let obj = {}


console.log(obj.__proto__ === Object.prototype); // true

/*
So we are just using native constructor functions when defining
literals

Native prototypes can also be modified, e.g. adding a method to
String.prototype
 */

String.prototype.show = function () {
    console.log(this)
};

"Hello".show();

/*
Prototypes are global so conflicts possible. Modifying native ones
is therefore usually a bad idea.

There is one accepted usecase: polyfilling.

This means making a substitute for a method that exists in the JS
specification, but isn't yet released - can implement this manually
 */

if (!String.prototype.yo) { // If no such method on proto, add it!
    String.prototype.yo = function(){
        return this + " yo"
    }
}

console.log("He".yo());

/*
Remember method borrowing, when a method from one object is used on
another that fulfills it's protocol (like duck typing in Python but
worse)

Can borrow methods from prototypes
 */

let test = {
    0: "Hello",
    1: "world!",
    length: 2,
};

test.join = Array.prototype.join;

console.log(test.join(', '));

/*
This works because the internal algorithm for the join built-in only
cares about the correct indices and the length property.
 */
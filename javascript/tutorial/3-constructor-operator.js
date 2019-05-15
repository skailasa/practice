/*
Constructors and New operator
 */

// Constructor functions
/*
Named with a capital letter, and are only executed with a
"new" operator
 */

function User(name) {
    this.name = name;
    this.isAdmin = false;
}

let user = new User("Jack");

console.log(user.name);
console.log(user.isAdmin);

/*
New empty object created by new, and assigned to `this`. The
function body executes, modifying this usually. the value of
this is returned.

Technically any function can be used as a constructor, which
is why we stick with convention.
 */

// Returning from constructors
/*
Usually constructors don't have a return statement, they write
their output to this. But if they do have it, output follows
rule:
1. If return is called with object, then this object is returned
instead of this.
2. If return is called with primitive, then it's ignored.
 */

// Can add methods to constructor too.

function User(name) {
    this.name = name;

    this.sayHi = function () {
        console.log("My name is: " + this.name);
    };
}


let sri = new User("sri");

sri.sayHi();
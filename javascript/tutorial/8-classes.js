/*
Yet another way of creating objects in JS, relatively new syntax though
 */

class User {
    constructor(name) {
        this.name = name;  // special method name
    }

    sayHi() {
        console.log(this.name)
    }
}


let u = new User('srinath');

u.sayHi();

/*
No comma between class methods, unlike object literals

- Unlike a function constructor, a class constructor cannot
be called without 'new'.
 */


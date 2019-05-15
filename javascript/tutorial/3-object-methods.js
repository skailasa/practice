/*
Properties that are functions are called methods in JS
 */

let user = {
    name: "Sri",
    age: 25
};

user.sayHi = function () {
  console.log("Hi!");
};

user.sound = 'Hi!';

user.sayHi();

// don't have to use function expression

function sayBye() {
    console.log("Bye!");
}
user.sayBye = sayBye;

user.sayBye();

// Shorter syntax in literal

let fruit = {
    colour: 'yellow',
    flavour() {
        console.log(`Tastes ${this.colour}`);
    }
};

fruit.flavour();

/*
This keyword works diffrently to c++ or other languages.
It's not bound to an object ...
 */

function yo() {
    console.log(this.name);
}

yo();

/*
It's value is evaluated at runtime, and could be anything
This is useful, allows the reuse of functions in multiple
objects.
 */

function greeting() {
    console.log(`${this.sound}`);
}

let animal = {
    sound: "woof"
};

user.greeting = greeting;
animal.greeting = greeting;

user.greeting();
animal.greeting();

/*
Arrow functions have no this, they are sort of anonymous
If you reference this from one, they reference an outer
this from a normal function
 */

let arrowExample = {
    name: "sri",
    sayHi() {
        let arrow = () => console.log(this.name);
        arrow();
    }
};

arrowExample.sayHi();

/*
New objects can be created with a function constructor

e.g.
new F()

if `F.prototype` is an object, then new uses it to set [[Prototype]] for the new
object.

Note, in this case it's just a regular property named prototype.
 */

let animal = {
    eats: true
};

function Rabbit(name) {
    this.name = name;
}

Rabbit.prototype = animal;

let rabbit = new Rabbit("White Rabbit");

console.log(rabbit.eats)

/*
I.e. when a new Rabbit is created, assign it's [[Prototype]] to animal.

Every function has the 'prototype' property even if it's not supplied.

e.g., Hare.prototype = { constructor: Hare };
 */

function Hare() {}

console.log(Hare.prototype.constructor === Hare);


function Dog() {
    Dog.prototype = {
        barks: true
    }
}


let puppy = new Dog();
console.log(puppy.constructor === Dog);


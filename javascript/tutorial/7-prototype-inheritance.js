/*
Often want to extend functionality, e.g. subclassing. Prototypal inheritance
is a JS way of achieving that.

 JS objects have a special property, prototype, that is either null or references
 another object - called the object's prototype.

 If we attempt to read a property from an object and it doesn't exist, we read it
 from it's prototype. Hence prototypal inheritance.
 */

let animal = {
    eats: true
};

let monkey = {
    climbs: true
};

// Protype is hidden and internal, can access with dunder
monkey.__proto__ = animal;

// This is a historical setter.

console.log(monkey.eats);

// Can write more idiomatically

let rabbit = {
    hops: true,
    __proto__: animal
};

console.log(rabbit.eats);

/*
Intuitively, prototypes are used only for reading properties. Write/delete
operations work directly with the object.

This is for data properties, not for accessors - getters/setters. If a property is a
getter/setter, then it then they are looked up in the prototype.
 */

let user = {
    _name: "John",

    set name(value) {
        this._name = value;
    },

    get name() {
        return `User's name is ${this._name}`;
    }
};

let admin = {
    __proto__: user,
    isAdmin: true
};

console.log(admin.name);

admin.name = "Sri";

// setter triggers from prototype
console.log(admin.name);

/*
What's the value of this? Is it tied to the 'admin' object or to it's prototype?

Ans: No matter where the method is found, in a method call, this is ALWAYS the
object before the dot.

 i.e. methods are shared, but NOT object state.

for ... in loop loops over inherited properties too
 */

for (let prop in admin) console.log(prop);





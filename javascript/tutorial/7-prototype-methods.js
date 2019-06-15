/*
Accessing __proto__ considered outdated. More modern methods to set
prototypes.

Have getters/setters and create methods for object prototypes.
 */

let animal = {
    eats: true
};

// create a new object with animal as it's prototype
let mouse = Object.create(animal);

console.log(mouse.eats); // true
console.log(Object.getPrototypeOf(mouse) === animal); // true

// change prototype
Object.setPrototypeOf(mouse, {});
console.log(Object.getPrototypeOf(mouse)); // {}

/*
Object.create has an optional second argument, property descriptors.

Can provide additional properties to the new object there
 */

let hare = Object.create(
    animal, {
        jumps: {
            value: true,
            writable: true,
            enumerable: false,
        }
    }
);

console.log(hare.jumps); // true

/*
Can use Object.create to perform object cloning more powerful than
copying over all properties.
 */

let obj = {
    name: "srinath"
};

// shallow clone of obj
let clone = Object.create(
    Object.getPrototypeOf(obj),
    Object.getOwnPropertyDescriptors(obj)
);
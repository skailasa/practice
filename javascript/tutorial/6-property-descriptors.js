/*
As in other OO languages JS has the concept of properties.

Besides a value, they have three other special attributes
    - called flags

- writable (bool) - otherwise read only property
- enumerable (bool) - otherwise, not listed in loops
- configurable (bool) - otherwise the property can't be deleted or modified
 */

// query all information about a property
let user = {
    name: "Sri"
};

// gives info on all flags
let descriptor = Object.getOwnPropertyDescriptor(user, 'name');

console.log(descriptor);

// can change these properties, i.e. make name readonly
Object.defineProperty(user, 'name', {writable: false});

user.name = 'john'; // doesn't error, but nothing happens

descriptor = Object.getOwnPropertyDescriptor(user, 'name');
console.log(descriptor);
console.log(user.name);

// Can create non-enumerable properties, for things like methods

let obj = {
    attribute: 'attribute',
    method () {
        return this.attribute;
    }
};

Object.defineProperty(obj, 'method', {enumerable: false});

for (let key in obj) console.log(key);

/*
Making a property non-configurable is a one-way street, can't change it back
because defineProperty doesn't work on non-configurable properties.
 */
/*
Allows us to construct strings from JS objects and back. Perfect
for sending complex data across networks.
 */

let student = {
    name: 'John',
    age: 21,
    isAdmin: false,
    courses: ['maths', 'physics']
};

let json = JSON.stringify(student);

console.log(json); // serialised json


/*
JS specific properties skipped by JSON for compatibility,
no serialisation of function properties, symbolic properties or
`undefined` properties.
 */


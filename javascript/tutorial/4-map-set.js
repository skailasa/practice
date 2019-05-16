/*
Map
- JS's hashtable
 */

let map = new Map(); // constructor
map.set('name', 'sri');
console.log(map.get('name'));

// Can use objects as keys

let sri = {name: 'sri', job: 'student'};

map.set(sri, 123);

console.log(map.get(sri));

/*
In JS the set call returns the map itself, even though it looks
inplace coming from Python. so we can chain calls
 */
map.set('1', 'a').set('2', 'b');


// Can create a map from an array or other iterable with key
// value pairs.

let map2 = new Map([
    ['1', true],
    ['2', false]
    ]);

console.log(map2.get('1'));

// Can instantiate a map from an object

let map3 = new Map(Object.entries({
    k1: 'val1',
    k2: 'val2'
}));

/*
Set
- standard set implementation in JS
 */

let s1 = new Set(); // constructor

let p1 = {name: 'n1'};
let p2 = {name: 'n2'};

s1.add(p1).add(p2); // method chaining

console.log(s1.size);

// iterate over set, in order of adding
for (let item of s1) {
    console.log(item.name);
}

/*
Weak maps and sets, are special in that they don't prevent
JS from removing its items from memory.

Allows one to catch objects that we want to be garbage collected
after their usage somewhere else.

Sort of like a C++ smart pointer, can guarantee that this will
be cleaned up.
 */


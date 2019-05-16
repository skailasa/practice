/*
Rest parameters
 - A function can be called with arbitrary numbers of args
 JS knows how many of these are actually used, and ignores the
 rest of them.

 The rest params can be mentioned in a function definition with
 an elipses. Literally, they mean 'gather all params into array'
 */


// for example, can gather all args into an array
// arrays are iterables so can use for ... of syntax
function sumAll(...args) {
    let sum = 0;

    for (let arg of args) sum += arg;

    return sum;
}

console.log(sumAll(1, 2, 3, 4, 5));

// rest parameters must be at the end to be parsed correctly
function testRest(arg1, ...args) {
    console.log(`arg1=${arg1}`);

    for (let arg of args) console.log(`${arg} from args`)
}

testRest(1, 2, 3, 4,);

/*
There is also a special array-like object named arguments which
contains all arguments by their index.
 */

function testArgs() {
    console.log(`There are ${arguments.length} args`);
    console.log(`The first one is ${arguments[0]}`);
}

testArgs('srinath', 'kailasa');

/*
`arguments` is array-like and iterable but NOT an array - does
not support array methods like .map() and always contains all
arguments, can't partially capture like with rest parameters.

Arrow functions don't support arguments
 */

/*
Spread operator

- Get parameters from an array (python *args)
 */

let arr = [3, 4, 5];

console.log(Math.max(...arr));

// can combine spread operator with normal values
console.log(Math.max(...arr, 1, 10,));

// Can be used to merge arrays
let merged = [0, ...arr];
console.log(merged);

// Works on any iterable
let str = 'test';
console.log([...str]);


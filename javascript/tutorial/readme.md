# Learning JavaScript

Using tutorials at [link](https://javascript.info/).

## Polyfills

Quite common for a given JS engine to only implement a part
of the standard.

When using modern language features, some engines fail to
support such code, have to use Babel - or something similar,
which is a *transpiler*. It rewrites modern JS into the
previous standard.

1.Modern build systems like webpack provide means to run
transpilers automatically on every code change, so easy
to integrate into dev process.

2. New language features may include new built-ins, and
syntax. Transpiler converts this back to old syntax, but
for new built-ins - have to implement them. A transpiler
that adds/updates functions is called polyfill.

## Garbage Collection

JS is GC, but still have to consider how this works. The
main concept is *reachability*. *Reachable* vals are those
accessible for use somehow, 
- Base set of inherently reachable vals, that can't be
deleted for obvious reasons.
    - Local variables and params of current function
    - Variables and parameters on the current chain of
    nested calls
    - Global variables
    - others (internal)
    
called roots

- Any other value is considered reachable if it's reachable
from a root by reference or by a chain of references.

GC removes all unreachable values for us.

## Object to Primitive Conversion

JS casts objects to primitives to force operations like
binary addition, or printing to stdout. All objects are true
in boolean contexts. Numeric conversion when we apply
mathematical functions, and string objects likewise occur in
string contexts (printing to console etc).

```javascript
obj1 = {
    p1: 'foo',
    p2: 42
}

obj2 = {
    p1: 'bar',
    p2: 1729
}

// conversion to string:
console.log(obj1) 
obj2[obj1] = 123; // using an object as a property key

// conversion to number
let num = Number(obj1);  // explicit conversion
let n = +obj1;  // unary plus
let delta = obj1 - obj2;
// comparison
let greater = obj1 > obj2;
```

`default` occurs in cases where the operator not sure how to
react. For example binary plus can concatenate strings as well
as add numbers, similar to weak comparison `==`, the type of
conversion is unclear.

To do conversion JS tries to find and call 3 methods.
1. `obj[Symbol.toPrimitive](hint)` if the method exists
2. if hint is `"string"`
    - try `obj.toString()` and `obj.valueOf()` whatever exists
3. if hint is `"number"` or `default`
    - try `obj.valueOf()` and `obj.toString()` whatever exists

We can implement a version of the first method for all of our
user defined objects.

```javascript
let user = {
    name: "Sri",
    wallet: 100,
    [Symbol.toPrimitive](hint) {
        console.log((`hint: ${hint}`);
        return hint == "string" ? `{name: "${this.name}"}`: this.wallet;
    }
}
```

No checking on type of returns in conversion. The only thing
that is checked is that a primitive is returned rather than
an object.

## Lexical Environment

Every scope has an associated hidden object called the
*Lexical Environment*. Consists of:
1. *Environment Record* - an object that stores all local
variables as it's properties (and other info like value of
`this`).
2. A reference to the *outer lexical environment*.

So a variable is a property of an internal object, to change
a variable means to change that property.

## Function Declaration

Unlike `let` variables, they are fully initialised not when
the execution reaches them, but earlier, when a LE created.
For top level functions this means the moment when the script
is started.

```javascript
// execution start
let str = "a";

function shout(name) {
    console.log(`${name} says ${str}`);
}
``` 

In the code above the lexical environment is non-empty from
the beginning. First it has `shout`, and later gets `str`
which is why we're allowed to use it in the function.`

When code wants to access a variable - the inner scope is
searched first, then the outer one, and so one until the
global one.

In strict mode, if nothing is found, it raises an error. 
However in regular JS, a new global variable is created.

So in the following example,

```javascript
let name = 'john'

function say() {
    console.log(`The name is ${name}`);
}

name = 'pete';

say();
```

the function accesses the most recent outer variable. So the
output is `The name is pete`.

## Closures

A closure is a function that remembers its outer variables
and can access them. In JS all functions are naturally
closures.

When a function declares other functions for example as a
part of its body, it's family of local variables is NOT
destroyed, and can be accessed by child functions. Closure,
'closed off', family of local variables.

```javascript
function makeAdder(a) {
    return function(b) {
        return a + b;
    };
}

var x = makeAdder(5);
var y = makeAdder(10);

console.log(x(6)); // 11
console.log(y(10)); // 20
```

In this case the garbage collector won't clean up these
local variables until all inner functions are no longer
being refered to.

Some engines might optimise this out, watch out for this.

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
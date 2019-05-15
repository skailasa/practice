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

 


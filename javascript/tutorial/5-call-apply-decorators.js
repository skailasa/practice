/*
Slow deterministic func slow(x). We probably want to cache this
output. Can wrap/decorate this
 */

function slow(x) {
    console.log(`called with ${x}`);
    return x;
}

function cachingDecorator(func) {
    let cache = new Map();

    return function(x) {
        if (cache.has(x)) {
            return cache.get(x);
        }

        let result = func(x);

        cache.set(x, result);
        return result;
    }
}

slow = cachingDecorator(slow);
slow(1);

/*
The above approach doesn't work with object methods. This is
because the wrapper doesn't have access to the `this` context.

Can fix this using func.call, allows the explicit setting of
the method call's context.
 */

// example

function sayHi() {
    console.log(this.name);
}

let user = {name: "user"};

sayHi.call(user);

// Using this logic

let worker = {
    someMethod() {
        return 1;
    },

    slow(x) {
        console.log(`called with ${x}`);
        return x * this.someMethod();
    }
};

function objectCachingDecorator(func) {
    let cache = new Map();
    return function (x) {
        if (cache.has(x)) {
            return cache.get(x);
        }
        let result = func.call(this, x);
        cache.set(x, result);
        return result;
    }
}

worker.slow = objectCachingDecorator(worker.slow); // decorate method
worker.slow(3);


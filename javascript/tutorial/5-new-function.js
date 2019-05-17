/*
One more way of creating functions, rarely used, sometimes
needed.
 */

let sum = new Function('a', 'b', 'return a + b');
console.log(sum(1, 2));

// with no args:
let shout = new Function("console.log('hey!')");
shout();

/*
Allows us to turn string literals into functions. Used for
example when receiving code from a server.

Doesn't reference the current lexical environment (scope) but
the global one.
 */

function getFunc() {
    let value = "test";

    let func = new Function(`console.log(value)`);

    return func;
}

// The above function won't work as func can't see value


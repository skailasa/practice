/*
Can bind not only `this` but also arguments with partial funcs
 */

// for example

function mul(a, b) {
    return a * b;
}

// null has been fixed as the context here, instead of `this`
let double = mul.bind(null, 2);

console.log(double(3)); // mul(2, 3)

/*
Currying, translates a function from a callable as f(a, b, c) to
f(a)(b)(c)
 */

function curry(f) {
    return function(a) {
        return function(b) {
            return f(a, b);
        }
    }
}

// usage
function sum(a, b) {
    return a + b;
}

let curriedSum = curry(sum);
console.log(curriedSum(1)(2));


/*
Allows for functions to both callable normally and partially
 */
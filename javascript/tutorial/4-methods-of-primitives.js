/*
Primitives as objects.

Desire to keep them small, and simple, but at the same time
incorporate a ton of functionality lead to object wrapprs. These
provide extra functionality before being destroyed
 */

let str = "Hello";

console.log(str.toUpperCase()); // HELLO

/*
Here the string is primitive, so when we access the property,
a special object is created that knows the value associated
with str, this is the object on which the methods are defined.
This method runs and returns a NEW string. The special object is
destroyed, leaving the primitive seemingly untouched.
 */

// Numbers
/*
All JS numbers are stored in doubles

Calling method on string literal needs two dots
 */

console.log(123..toString());

// gotcha, loss of precision
console.log( 0.1 + 0.2 === 0.3 ); // false

// can overcome
let sum = 0.1 + 0.2;
console.log(+sum.toFixed(2) == 0.30);

// self-increasing number!
console.log( 9999999999999999 ); // shows 10000000000000000

// NaNs are unique in that they don't equal anything, even
// themselves
console.log(NaN === NaN);

// Strings
/*
JS strings are immutable.

Can do some strange things due to polymorphism of mathematical
operators on strings.
 */

// lower case always greater than upper case
console.log('a' > 'A'); // true

// Have to use some other libs for string comparisons
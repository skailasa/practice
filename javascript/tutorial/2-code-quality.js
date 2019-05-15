/*
Style guide for JS
 */

// Curly Braces
/*
JS projects use egyptian style, with opening brace
on the same line as the corresponding keyword.
 */

let x = true;
if (x) {
   console.log("wow!");
}

// Horizontal indents should be 2 or 4 spaces

// Semicolons after each statement

// Avoid too much nesting, instead of ...

for (let i = 0; i < 5; i++) {
    if (x) {
        console.log("foo");
    }
}

// Do ...

for (let i = 0; i < 10; i++) {
    if (!x) continue;
    console.log("foo");
}

// Instead of ...

function power(x, n) {
    if (n < 10) {
        console.log("Negative nums not supported");
    } else {
        let res = 1;

        for (let i = 0; i < n; i++) {
            res *= x;
        }
        return res;
    }
}

// Do ...

function power2(x, n) {
    if (n < 0) {
        console.log("Negative nums not supported");
        return;
    }
    let res = 1;

    for (let i = 0; i < n; i++) {
        res *= x;
    }
    return res;
}

// Function declarations go at bottom of file by convention

/*
Iterables
 */

// Similar to many OO languages

// Create range object
// Need to add a method called Symbol.iterator to this object
function Range (from, to) {
    this.from = from;
    this.to = to;
    this[Symbol.iterator] = rangeIterator;
}


// 1. call to for..of calls this function
function rangeIterator () {

    // ... returns an iterator object
    // 2. Onward, for..of works only with this iterator, asking
    // for the next values
    return {
        current: this.from,
        last: this.to,

        // 3. next() called on each iteration
        next() {
            // 4. returns value as an object
            if (this.current <= this.last) {
                return {done: false, value: this.current++};
            } else {
                return {done: true};
            }
        }
    }
}

let range = new Range(1, 5);

console.log(range[Symbol.iterator]);

for (let num of range) {
    console.log(num);
}

// String is an iterable
for (let char of "foo") {
    console.log(char);
}

// Calling an iterator explicitly

let str = "Hello";

let iterator = str[Symbol.iterator]();

while (true) {
    let res = iterator.next();
    if (res.done) break;
    console.log(res.value);
}


// Rarely used, but gives some more control than for..of
// syntax

// Iterables and array-likes
/*
- Iterables are objects that implement the Symbol.iterator
method
- Array-likes are objects that have indices and length - hence
look like arrays.
- Objects can satisfy both (strings)
 */

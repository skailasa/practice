/*
When a function (foo) declares other functions (bar and baz),
the family of local variables created in foo is not destroyed
when the function exits. The variables merely become invisible
to the outside world. Foo can therefore cunningly return the 
functions bar and baz, and they can continue to read, write and 
communicate with each other through this closed-off family of 
variables ("the closure") that nobody else can meddle with, not
 even someone who calls foo again in future.

 https://stackoverflow.com/questions/111102/how-do-javascript-closures-work
*/

function makeAdder(a) {
    return function(b) {
      return a + b;
    };
  }
  var x = makeAdder(5);
  var y = makeAdder(20);

console.log(x(6)); // 11
console.log(y(7)); // 27


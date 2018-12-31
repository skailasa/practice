/* 
Prototyping is a powerful way to construct objects
in JS. Forms part of a lookup chain, if method doesn't
exist on an object, interpreter will check it's prototype.

JS lets you modify an object's prototype at any time
during a program, which means additional methods can
be added to an object at runtime.
*/
function Person(first, last) {
    this.first = first;
    this.last = last;
  }
  Person.prototype.fullName = function() {
    return this.first + ' ' + this.last;
  };
  Person.prototype.fullNameReversed = function() {
    return this.last + ', ' + this.first;
  };

var s = new Person('Srinath', 'Kailasa');
// s.firstNameCaps(); // TypeError on line 1: s.firstNameCaps is not a function

Person.prototype.firstNameCaps = function() {
  return this.first.toUpperCase();
};
console.log(s.firstNameCaps())

/*
Can also do this to built in objects
*/

var name = 'Srinath';

String.prototype.reversed = function() {
    var res = '';
    for (var i=this.length-1; i>=0; i--) {
        res += this[i];
    }
    return res
}

console.log(name.reversed())

// even works on string literals now

console.log('Srinath'.reversed())
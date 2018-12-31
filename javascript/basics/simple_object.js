/*
Objects in JS are not declared with class statements,
instead it's a prototype language.
*/

function Person(first, last) {
    // A simple JS object
    return {
      first: first,
      last: last,
      fullName: function() {
        return this.first + ' ' + this.last;
      },
      fullNameReversed: function() {
        return this.last + ', ' + this.first;
      }
    };
  }

function personFullName() {
  return this.first + ' ' + this.last
}

function personFullNameReversed() {
  return this.last + ' ' + this.first
}

function BetterPerson(first, last) {
  // better implementation using `this` keyword
  this.first = first;
  this.last = last;
  this.fullName = personFullName;
  this.fullNameReversed = personFullNameReversed;
}

var oldme = Person('Srinath', 'Kailasa')


// new creates a new object, strongly related to this
// Functions designed to be called by new are called
// constructor functions.
var me = new BetterPerson('Srinath', 'Kailasa')
console.log(me.fullName())
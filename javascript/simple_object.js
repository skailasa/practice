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

var me = Person('Srinath', 'Kailasa')

console.log(me.fullName())
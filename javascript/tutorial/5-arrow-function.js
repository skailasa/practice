/*
for functions we don't want to really leave the current context.
 */

// Arrow functions don't have a this, if it is accessed it's
// taken from the outer scope

let group = {
    title: "Our group",
    students: ["John", "Pete"],

    showList() {
        this.students.forEach(
            student => console.log(this.title + ': ' + student)
        )
    }
};

group.showList();

// Have no arguments variable, and take this from outer scope
// if deployed in a function - consider the following decorator

function defer(f, ms) {
    return function () {
        setTimeout(() => f.apply(this, arguments), ms)
    }
}

function yo(who) {
    console.log(`yo ${who}`)
}

let deferredYo = defer(yo, 100);

deferredYo('Sri');

// c.f. with
/*
function defer(f, ms) {
  return function(...args) {
    let ctx = this;
    setTimeout(function() {
      return f.apply(ctx, args);
    }, ms);
  };
}
*/


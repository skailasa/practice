/*
Once a method is passed somewhere separately from the object,
`this` context is lost. Therefore can bind methods to correct
context, using function binding.
 */


let user = {
    name: "Sri"
};

function func() {
    console.log(this.name);
}

let funcUser = func.bind(user); // bind to user object

funcUser(); // will always call on user obj

/*
Can do the same thing for methods defined on objects
 */

let betterUser = {
    name: "Sri",
    sayHi() {
        console.log(`Hello I am ${this.name}`);
    }
};

// bind to betterUser object

let sayHiBound = betterUser.sayHi.bind(betterUser);
sayHiBound();



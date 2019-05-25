/*
Syntax for getters and setters in JavaScript. work on 'accessor'
propeties, in comparison to the data properties considered so far.
Accessor properties are defined in terms of getters and setters.
 */

let obj = {
    property: 'property name',
    get propertyName(){
        return this.property
    },
    set propertyName(value) {
        this.property = value;
    }
};

let instance = obj;

obj.propertyName = 'new name';

console.log(obj.propertyName);

/*
Accessor properties are different - as compared to data properties in
that they have different descriptors.

- they don't have writable - as they are writable if they have a setter
- have a getter and setter, otherwise are the same (configurable/enumerable)
 */


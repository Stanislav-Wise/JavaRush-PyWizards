let person = {
    name: "Bob",
    age: 28,
    isAdmin: true,
    address: {
        street: "Ленина",
        number: 9,
    },

    city: ["Moscow", "Tula", "Sochi"],
    sayHi: function () {
        console.log(`Привет, ${this.age}`);
    },
    sayBy: function () {
        console.log(`Пока, ${person.name}`)
    }
};

console.log("+++++++++++++")
person.sayHi();
person.sayBy();

console.log("+++++++++++++")
// let user = person;
let user = {...person};
user.sayHi();
user.sayBy();

console.log("+++++++++++++")
person.name = 'Ann';
person.age = 35;

console.log(person)
console.log(user)
console.log("+++++++++++++")
user.sayHi();
user.sayBy();
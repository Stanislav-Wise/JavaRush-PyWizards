function Person(name, age) {
    this.name = name;
    this.age = age;
    this.sayHi = function () {
        console.log(`Привет, ${this.name}`);
    };
}

let user1 = new Person("Ann", 29);
let user2 = new Person("Bob", 34);

console.log(user1);
console.log(user2);

user1.name = "Alisa"
user1.sayHi()
user2.sayHi()

console.log(user1);
console.log(user2);
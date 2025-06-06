class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    sayHi() {
        console.log(`Привет, ${this.name}`);
    }
    sayBy() {
        console.log(`Пока, ${this.name}`)
    }
}


let user1 = new User("Bob", 23)
let user2 = new User("Ann", 27)

user1.sayHi()
user2.sayHi()

user1.sayBy()
user2.sayBy()

console.log(user1.name)
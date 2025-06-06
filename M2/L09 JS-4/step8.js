class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    get age() {
        return this._age
    }

    set age(value) {
        if (value < 0) {
            console.log("Возраст не может быть меньше 0");
            value = 0;
        }
        return this._age = value;
    }

    static add(a, b) {
        return a + b;
    }

    sayHi() {
        console.log(`Привет, ${this.name}`);
    }
    sayBy() {
        console.log(`Пока, ${this.name}`)
    }
}


let user1 = new User("Bob", 23);
let user2 = new User("Ann", 27);

user1.sayHi();
user2.sayHi();

user1.sayBy();
user2.sayBy();


console.log(user1.age);
user1.age = 100;

console.log(user1.age);

user1.age = -10;

console.log(user1.age);

console.log(User.add(2, 3))
let person = {
    name: "Bob",
    age: 28,
    isAdmin: true,
    address: {
        street: "Ленина",
        number: 9.
    },
    // город: "Moscow"
    city: ["Moscow", "Tula", "Sochi"]


};

console.log(person)
// console.log(person.город)


let user = new Object();
user.name = 'Ann';
user.age = 21;
console.log(user)

user.age = 25;
console.log(user)

console.log(user.name);
console.log(person.name);

let my_name = "name"

console.log("+++++++++++++++++++");
console.log(user[my_name]);

console.log(user.my_name);

console.log(person["name"]);
console.log("+++++++++++++++++++");
console.log(user);

console.log("+++++++++++++++++++");
console.log("+++++++++++++++++++");

person.job = "Программист";
console.log(person);

person.job = "Продавец";
console.log(person);

delete person.age;
console.log(person);

console.log("name" in person)
console.log("name12" in person)
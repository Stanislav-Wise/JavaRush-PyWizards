let animal = {
    eats: true,
    walk() {
        console.log("Животное идет");
    }
};

let rabbit = {
    jumps: true
};

// rabbit.__proto__ = animal;
console.log(rabbit.jumps);
// console.log(rabbit.eats)
// console.log(rabbit.qaz)
// console.log(rabbit.walk())

console.log(rabbit.__proto__ === animal)
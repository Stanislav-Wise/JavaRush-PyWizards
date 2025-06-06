let person = {
    name: "Bob",
    sayHi() {
        console.log("Привет!", this.name);
    }
};
person.sayHi();
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


for (let key in person) {
    console.log(key, ":", person[key]);
}
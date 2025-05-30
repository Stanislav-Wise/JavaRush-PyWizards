// &&  || !

let age = 15;
let hasPassport = false;

let canTravel = age >= 18 && hasPassport;  // AND
console.log(canTravel)
// console.log(age + hasPassport)

let canTravel1 = age >= 18 || hasPassport; // OR
console.log(canTravel1)


let canTravel2 = (age >= 18 || hasPassport) && (age >= 18 || hasPassport) ; // OR
console.log(canTravel1)
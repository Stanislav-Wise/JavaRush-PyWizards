let alp = ["A","B", "C", "D", "E"];

console.log(alp);
console.log(alp.length);

alp.push("Z");
console.log(alp);
console.log(alp.length);

let myStr = alp.pop();
console.log(alp);
console.log(alp.length);
console.log(myStr);

let myStr2 = alp.shift(myStr);
console.log(alp);
console.log(alp.length);
console.log(myStr2);

alp.unshift(myStr);
console.log(alp);
console.log(alp.length);


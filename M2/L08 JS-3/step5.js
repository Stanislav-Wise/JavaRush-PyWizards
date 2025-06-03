let num = Number(prompt("Введи число: "));
let sum = 0;
while (num !== 0) {
    alert(`Вы ввели ${num}`);
    sum += num;
    num = Number(prompt("Введи число: "));
}
alert(`Сумма равна ${sum}`)

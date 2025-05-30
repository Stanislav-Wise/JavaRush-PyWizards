let userName = prompt('Как тебя зовут?');
let userAge = prompt('Сколько тебе лет?');

let age = Number(userAge);

if (age >= 18) {
    alert(`Вход разрешен, ${userName}`);
    if (userName == 'Bob') {
        alert(`Привет, ${userName}`);
    }
} else {
    alert(`Вход запрещен, ${userName}`);
}
let day = prompt('Введите день недели')

switch (day) {
    case "1":
        alert(`Понедельник`);
        break;
    case "2":
        alert(`Вторник`);
        break;
    case "3":
        alert(`Ср`);
        break;
    case "4":
        alert(`Чт`);
        break;
    case "5":
        alert(`Пт`);
        break;
    case "6":
        alert(`Сб`);
        break;
    case "7":
        alert(`Вс`);
        break;
    default:
        alert(`нет такого значения`);
}

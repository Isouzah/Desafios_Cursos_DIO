let nome = "Neutrun";
let xp = 5570;
let nível;

if (xp <= 1000) {
    nível = "Ferro";
}
else if  (xp > 1000 && xp <= 2000) {
    nível = "Bronze";
}
else if  (xp > 2000 && xp <= 5000) {
    nível = "Prata";
}
else if  (xp > 5000 && xp <= 7000) {
    nível = "Ouro";
}
else if  (xp > 7000 && xp <= 8000) {
    nível = "Platina";
}
else if  (xp > 8000 && xp <= 9000) {
    nível = "Ascendente";
}
else if  (xp > 9000 && xp <= 10000) {
    nível = "Imortal";
}
else if  (xp > 10000) {
    nível = "Radiante";
}
console.log("O Herói de nome " +nome +" está no nível de " +nível)
let PlayerName = "Neutrun"
let level
let RankedPoints

function LevelCalculator ( win , loss){
    return win - loss
}
RankedPoints = LevelCalculator (170,12)

if (RankedPoints <= 10){
    level = "Ferro";
}
else if  (RankedPoints > 10 && RankedPoints <= 20) {
    level = "Bronze";
}
else if  (RankedPoints > 20 && RankedPoints <= 50) {
    level = "Prata";
}
else if  (RankedPoints > 50 && RankedPoints <= 80) {
    level = "Ouro";
}
else if  (RankedPoints > 80 && RankedPoints <= 90) {
    level = "Diamante";
}
else if  (RankedPoints > 90 && RankedPoints <= 100) {
    level = "Lendário";
}
else if  (RankedPoints > 100)
    level = "Imortal";


console.log("O Jogador "+ PlayerName +" tem de saldo de "+ RankedPoints +" vitórias e está no nível de " + level);
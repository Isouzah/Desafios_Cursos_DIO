class Heroi {
    constructor (nome, idade, classe){
        this.nome = nome;
        this.idade = idade;
        this.classe = classe;
        this.ataque = '';
    if (classe === "guerreiro"){
        this.ataque = "espada";}
    else if (classe === "mago"){
        this.ataque = "magia";}
    else if (classe === "monge"){
        this.ataque = "artes marciais";}
    else if (classe === "ninja"){
        this.ataque = "shuriken";}
    }

    atacar() {
    console.log(`O ${this.nome} atacou usando ${this.ataque}`);
    }
}
let escolhido = new Heroi ("Shura", 42, "espada");
escolhido.atacar();
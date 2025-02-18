class heroi {
    constructor (nome, idade, classe)
        this.nome = nome
        this.idade = idade
        this.classe = classe [guerreiro, mago, monge, ninja]
        this.ataque={
    switch(ataque){
        case 'guerreiro':
            ataque = espada
            break
        case 'mago':
            ataque = magia
            break
        case 'monge':
            ataque = artes marciais
            break
        case 'ninja':
            ataque = shuriken
    }
}
    atacar(){
        console.log(`O $this.nome atacou usando $ataque`)
    }
}

let escolhido = new heroi (Aldebaran, 42, guerreiro)

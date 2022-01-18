var altura = 0
var largura = 0
var vidas = 1


function detectorDaAreaDisponivelDoJogo() {
    altura = window.innerHeight
    largura = window.innerWidth
    console.log(largura, altura)
}


detectorDaAreaDisponivelDoJogo()


function criandoPosicaoRandomica() {
    // Removendo o mosquito anterior (caso exista)
    if (document.getElementById('mosquito')) {
        document.getElementById('mosquito').remove()
        if (vidas > 3) {
            window.location.href = 'fim_de_jogo.html'
        } else {
            document.getElementById('vida' + vidas).src = 'img/coracao_vazio.png'
            vidas++
        }
    }
    

    var posicaoX = Math.floor(Math.random() * largura) - 90   // é necessário diminuir o valor em píxel que o elemento ocupa
    var posicaoY = Math.floor(Math.random() * altura) - 90 //  Explicação: Aula 225 - 14:50 minutos

    posicaoX = posicaoX < 0 ? 0 : posicaoX // Operador ternário para evitar que algum número negativo seja apresentado
    posicaoY = posicaoY < 0 ? 0 : posicaoY  // Operador ternário para evitar que algum número negativo seja apresentado

    // Criando o elemento html no caso a imagem do mosquito
    var mosquito = document.createElement('img') // Criando uma tag de img no html usando o javascript
    mosquito.src = 'img/mosquito.png' // Utilizando a propriedade scr da tag <img> 'img' criada, e definindo o endereço da img
    mosquito.className = tamanhoAleatorioMosquito() + ' ' + ladoSurgimentoMosquito() // Adicionando uma classe a tag que foi atribuida a variável correspondente
    mosquito.style.left = posicaoX + 'px' // Defindo um estilo de deslocamento a esquerda com a coordenada aleatória gerada
    mosquito.style.top = posicaoY + 'px' // Defindo um estilo de deslocamento para cima com a coordenada aleatória gerada
    mosquito.style.position = 'Absolute' // Definindo uma posição absoluta ao estilo, apra que o deslocamento tenha efeito
    mosquito.id = 'mosquito'
    mosquito.onclick = function () {
        this.remove()
    }

    document.body.appendChild(mosquito) // Acessando o body da nossa pagina, e adicionando um filho a ele


    console.log(posicaoX , posicaoY)
    console.log(ladoSurgimentoMosquito())
}


function tamanhoAleatorioMosquito() {
    var classe = Math.floor(Math.random() * 3)
    switch (classe) {
        case 0:
            return 'mosquito1'
        case 1:
            return 'mosquito2'
        case 2:
            return 'mosquito3'
    }
}


function ladoSurgimentoMosquito() {
    var lado = Math.floor(Math.random() * 2)

    switch (lado) {
        case 0:
            return 'ladoA'
        case 1:
            return 'ladoB'
    }
}
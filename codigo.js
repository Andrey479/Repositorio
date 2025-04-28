const botao = document.querySelector("#botao");
const mensagem = document.querySelector("#mensagem");
let contador = 1;

/*para garantir que a mensagem só apareça uma vez*/
if (contador = 1)
    {
        botao.addEventListener("click", () => {
            mensagem.style.display = "block";});
        contador++;
    }

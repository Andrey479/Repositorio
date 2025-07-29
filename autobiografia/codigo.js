const botao = document.querySelector("#botao");
const mensagem = document.querySelector("#mensagem");

//se clicar mais de uma vez a mensagem some
botao.addEventListener("click", () => 
{
    if (mensagem.style.display === "block")
        mensagem.style.display = "none";
    else
        mensagem.style.display = "block";
});

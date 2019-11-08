let botao = document.querySelector("#bthome");

function tirarClass(){
    if (botao.classList.contains("bthome")){
        botao.classList.remove("bthome");

} else{
    botao.classList.add("bthome")
}
}

botao.onclick = tirarClass;


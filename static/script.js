const form = document.getElementById("form");

const resultado = document.getElementById("resultado");

const loading = document.getElementById("loading");

const linkFinal = document.getElementById("linkFinal");

const copiar = document.getElementById("copiar");

form.addEventListener("submit", async (e)=>{

    e.preventDefault();
    resultado.classList.add("hidden");
    loading.classList.remove("hidden");

    const long_url=document.getElementById("url").value;
    
    try{

        const resposta = await fetch("http://127.0.0.1:5000/api/encurtar",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                long_url
            })
        });

        const dados = await resposta.json();
        loading.classList.add("hidden");

        if(!resposta.ok){
            alert(dados.erro);
            return;
        }

        resultado.classList.remove("hidden");
        linkFinal.value=dados.url_completa;
    }

    catch{
        loading.classList.add("hidden");
        alert("Não foi possível conectar ao servidor.");
    }

});

copiar.addEventListener("click",async()=>{
    await navigator.clipboard.writeText(linkFinal.value);
    copiar.innerText="Copiado!";
    setTimeout(()=>{
        copiar.innerText="Copiar";
    },1500);
});
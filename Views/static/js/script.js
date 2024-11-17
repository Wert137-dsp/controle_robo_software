
window.onload = function(){

    eixoA = document.getElementById("eixo_a")
    eixoB = document.getElementById("eixo_b")
    eixoC = document.getElementById("eixo_c")
    eixoD = document.getElementById("eixo_d")
    eixoE = document.getElementById("eixo_e")
    eixoF = document.getElementById("eixo_f")

    btnSalvar = document.getElementById("moveBtn")

    function salvarPosicao(){

        fetch("/salvarPosicao",{

            method: "POST",
            headers: {

                "Content-Type" : "application/json"
            },
            body: JSON.stringify({

                eixoA: eixoA.valor,
                eixoB: eixoB.valor,
                eixoC: eixoC.valor,
                eixoD: eixoD.valor,
                eixoE: eixoE.valor,
                eixoF: eixoF.valor
            })
        })
        .then(response => response.json())
        .then(data =>{

            console.log("Ok")
        })
        .catch(error => {

            console.log("Erro ao salvar")
        })
    }

    function enviarEixo(id, valor){

        fetch("/enviarEixo",{

            method: "POST",
            headers: {

                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                eixo: id,
                valor: valor
            })
        })
        .then(response => response.json())
        .then(data =>{

            console.log(id+" --- "+data)
        })
        .catch(error =>{

            console.log("Erro ao enviar por eixo "+id)
        })
    }

    console.log(eixoA)
    eixoA.addEventListener("input", function(){

        console.log("Eixo A: "+eixoA.value)

       enviarEixo(eixoA.id, eixoA.value)
    })

    eixoB.addEventListener("input", function(){

        console.log("Eixo B: "+eixoB.value)
        enviarEixo(eixoB.id, eixoB.value)
    })

    eixoC.addEventListener("input", function(){

        console.log("Eixo C: "+eixoC.value)
        enviarEixo(eixoC.id, eixoC.value)
    })

    eixoD.addEventListener("input", function(){

        console.log("Eixo D: "+eixoD.value)
        enviarEixo(eixoD.id, eixoD.value)
    })

    eixoE.addEventListener("input", function(){

        console.log("Eixo E: "+eixoE.value)
        enviarEixo(eixoE.id, eixoE.value)
    })

    eixoF.addEventListener("input", function(){

        console.log("Eixo F: "+eixoF.value)
        enviarEixo(eixoF.id, eixoF.value)
    })

}


/*

{
    eixo: "EixoA",
    value: "34"
}

*/

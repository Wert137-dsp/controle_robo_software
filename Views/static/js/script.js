
window.onload = function(){

    eixos = []

    var index_selected

    eixoA = document.getElementById("eixo_a")
    eixoB = document.getElementById("eixo_b")
   /* eixoC = document.getElementById("eixo_c")
    eixoD = document.getElementById("eixo_d")
    eixoE = document.getElementById("eixo_e")
    eixoF = document.getElementById("eixo_f")*/

    nomePosicao = document.getElementById("nomePosicao")
    btnSalvar = document.getElementById("saveBtn")
    btnMover = document.getElementById("moveBtn")
    btnAssistente = document.getElementById("btnAssistente")


    selectPosition = document.getElementById("select_position")

    console.log(selectPosition)

    function getPosicoes(){
        selectPosition.innerHTML = "";
        var option = document.createElement("option")
        selectPosition.appendChild(option)
       
        fetch("/getPosicoes", {method: "POST"})
        .then(response => response.json())
        .then(data => {

           
            data.forEach(element => {
                console.log(element.nome); // Exibe o valor de "nome" no console
            
                // Cria um novo elemento <option>
                const option = document.createElement("option");
            
                // Define o texto exibido e o valor do <option>
                option.textContent = element.nome; // Texto exibido
                option.id = element.id_posicao;    // ID único, se necessário
                option.value = element.nome;      // Valor que será enviado no formulário
            
                // Adiciona o <option> ao <select>
                selectPosition.appendChild(option);

                eixos.push(element)
                console.log(eixos)
            });
        })
        .catch(error =>{

            console.log(error)
        })
    }

    selectPosition.addEventListener("change", function(event){

        var id = event.target.selectedIndex
        index_selected = id
        eixoA.value = eixos[id-1].eixoA
        eixoB.value = eixos[id-1].eixoB
       /* eixoC.value = eixos[id-1].eixoC
        eixoD.value = eixos[id-1].eixoD
        eixoE.value = eixos[id-1].eixoE
        eixoF.value = eixos[id-1].eixoF*/

    })


    function salvarPosicao(){

        fetch("/salvarPosicao",{

            method: "POST",
            headers: {

                "Content-Type" : "application/json"
            },
            body: JSON.stringify({
                nome: nomePosicao.value,
                eixoA: eixoA.value,
                eixoB: eixoB.value,
               /* eixoC: eixoC.value,
                eixoD: eixoD.value,
                eixoE: eixoE.value,
                eixoF: eixoF.value*/
            })
        })
        .then(response => response.json())
        .then(data =>{

            alert(data.message)

            getPosicoes()
        })
        .catch(error => {

            
            console.log("Erro ao salvar")
            alert(error)
        })
    }

    function moverRobo(eixo){

        fetch("/moverRobo",{

            method: "POST",
            headers: {

                "Content-Type" : "application/json"
            },
            body: JSON.stringify({
                eixoA: eixoA.value,
                eixoB: eixoB.value,
              /*  eixoC: eixoC.value,
                eixoD: eixoD.value,
                eixoE: eixoE.value,
                eixoF: eixoF.value*/
            })
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

    
    btnAssistente.addEventListener("click", function(){
        fetch("/checarComando", {method: "POST"})
    })


    btnSalvar.addEventListener("click", function(){
        if(!(nomePosicao.value == "")){

            salvarPosicao()
        }else{

            nomePosicao.onFocus()
        }
        
    })

    btnMover.addEventListener("click", function(){

        moverRobo();
    })

    eixoA.addEventListener("input", function(){

        console.log("Eixo A: "+eixoA.value)

        fetch("/enviarEixo",{

            method: "POST",
            headers: {

                "Content-Type" : "application/json"
            },
            body: JSON.stringify({
                eixoA: eixoA.value,
                
            })
        })
    })

    eixoB.addEventListener("input", function(){

        console.log("Eixo B: "+eixoB.value)
        fetch("/enviarEixo",{

            method: "POST",
            headers: {

                "Content-Type" : "application/json"
            },
            body: JSON.stringify({
                eixoB: eixoB.value,
                
              
            })
        })
    })
/*
    eixoC.addEventListener("input", function(){

        console.log("Eixo C: "+eixoC.value)
       moverRobo()
    })

    eixoD.addEventListener("input", function(){

        console.log("Eixo D: "+eixoD.value)
        moverRobo()
    })

    eixoE.addEventListener("input", function(){

        console.log("Eixo E: "+eixoE.value)
        moverRobo()
    })

    eixoF.addEventListener("input", function(){

        console.log("Eixo F: "+eixoF.value)
        moverRobo()
    })*/

    getPosicoes();

   /* setInterval(() => {
        fetch("/checarComando", {method: "POST"})
    }, 5000);*/
}


/*

{
    eixo: "EixoA",
    value: "34"
}

*/

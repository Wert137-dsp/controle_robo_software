
window.onload = function(){

    eixos = []

    var index_selected

    eixoA = document.getElementById("eixo_a")
    eixoB = document.getElementById("eixo_b")
    eixoC = document.getElementById("eixo_c")
    eixoD = document.getElementById("eixo_d")
    eixoE = document.getElementById("eixo_e")
    eixoF = document.getElementById("eixo_f")

    nomePosicao = document.getElementById("nomePosicao")
    btnSalvar = document.getElementById("saveBtn")
    btnMover = document.getElementById("moveBtn")

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
        eixoA.value = eixos[id-1].eixo1
        eixoB.value = eixos[id-1].eixo2
        eixoC.value = eixos[id-1].eixo3
        eixoD.value = eixos[id-1].eixo4
        eixoE.value = eixos[id-1].eixo5
        eixoF.value = eixos[id-1].eixo6

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
                eixoC: eixoC.value,
                eixoD: eixoD.value,
                eixoE: eixoE.value,
                eixoF: eixoF.value
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

    function moverRobo(){

        fetch("/moverRobo",{

            method: "POST",
            headers: {

                "Content-Type" : "application/json"
            },
            body: JSON.stringify({
                eixoA: eixoA.value,
                eixoB: eixoB.value,
                eixoC: eixoC.value,
                eixoD: eixoD.value,
                eixoE: eixoE.value,
                eixoF: eixoF.value
            })
        })
        .then(response => response.json())
        .then(data =>{

           console.log(data.messate)
        })
        .catch(error => {

            
            console.log("Erro ao mover")
            alert(error)
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

    getPosicoes();

    setInterval(() => {
        fetch("/checarComando", {method: "POST"})
    }, 5000);
}


/*

{
    eixo: "EixoA",
    value: "34"
}

*/

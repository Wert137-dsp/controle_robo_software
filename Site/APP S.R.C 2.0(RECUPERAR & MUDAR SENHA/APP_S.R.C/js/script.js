
// Seleciona o botão de "sign in" pelo seu ID
var btnSignin = document.querySelector("#signin");

// Seleciona o botão de "sign up" pelo seu ID
var btnSignup = document.querySelector("#signup");

// Seleciona o elemento <body> da página
var body = document.querySelector("body");

// Adiciona um ouvinte de evento ao botão de "sign in"
// Quando clicado, muda a classe do <body> para "sign-in-js"
btnSignin.addEventListener("click", function () {
    body.className = "sign-in-js"; // Altera a classe do body para 'sign-in-js'
});

// Adiciona um ouvinte de evento ao botão de "sign up"
// Quando clicado, muda a classe do <body> para "sign-up-js"
btnSignup.addEventListener("click", function () {
    body.className = "sign-up-js"; // Altera a classe do body para 'sign-up-js'
});

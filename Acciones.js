// let p1 = document.getElementById("p1");
// let p2 = document.getElementById("p2");
// let p3 = document.getElementById("p3");
// let p4 = document.getElementById("p4");
// let p5 = document.getElementById("p5");
// let p6 = document.getElementById("p6");
// let p7 = document.getElementById("p7");

// let estf1 = false;
// let estf2 = false;
// let estf3 = false;
// let estf4 = false;
// let estf5 = false;
// let estf6 = false;
// let estf7 = false;

let SubS1 = document.getElementById("SubS1");
let SubS2 = document.getElementById("SubS2");
let SubS3 = document.getElementById("SubS3");

let comidas = document.getElementById("comidas");
let bebidas = document.getElementById("bebidas");
let postres = document.getElementById("postres");

let estC1 = false;
let estC2 = false;
let estC3 = false;

// function mostrarTexto1() {
//     if (estf1 == false) {
//         estf1 = true;
//         p1.style.display = "flex";
//     } else {
//         estf1 = false;
//         p1.style.display = "none";
//     }
// }

// function mostrarTexto2() {
//     if (estf2 == false) {
//         estf2 = true;
//         p2.style.display = "flex";
//     } else {
//         estf2 = false;
//         p2.style.display = "none";
//     }
// }

// function mostrarTexto3() {
//     if (estf3 == false) {
//         estf3 = true;
//         p3.style.display = "flex";
//     } else {
//         estf3 = false;
//         p3.style.display = "none";
//     }
// }

// function mostrarTexto4() {
//     if (estf4 == false) {
//         estf4 = true;
//         p4.style.display = "flex";
//     } else {
//         estf4 = false;
//         p4.style.display = "none";
//     }
// }

// function mostrarTexto5() {
//     if (estf5 == false) {
//         estf5 = true;
//         p5.style.display = "flex";
//     } else {
//         estf5 = false;
//         p5.style.display = "none";
//     }
// }

// function mostrarTexto6() {
//     if (estf6 == false) {
//         estf6 = true;
//         p6.style.display = "flex";
//     } else {
//         estf6 = false;
//         p6.style.display = "none";
//     }
// }

// function mostrarTexto7() {
//     if (estf7 == false) {
//         estf7 = true;
//         p7.style.display = "flex";
//     } else {
//         estf7 = false;
//         p7.style.display = "none";
    }
}

function mostrarComidas1() {
    if (estC1 == false) {
        estC1 = true;
        SubS1.style.display = "flex";
        comidas.style.width = "90%";
        bebidas.style.display = "none";
        postres.style.display = "none";
    } else {
        estC1 = false;
        SubS1.style.display = "none";
        comidas.style.width = "25%";
        bebidas.style.display = "flex";
        bebidas.style.flexDirection = "column";
        postres.style.display = "flex";
        postres.style.flexDirection = "column";
    }
}

function mostrarComidas2() {
    if (estC2 == false) {
        estC2 = true;
        SubS2.style.display = "flex";
        bebidas.style.width = "90%";
        postres.style.display = "none";
        comidas.style.display = "none";
    } else {
        estC2 = false;
        SubS2.style.display = "none";
        bebidas.style.width = "25%";
        postres.style.display = "flex";
        postres.style.flexDirection = "column";
        comidas.style.display = "flex";
        comidas.style.flexDirection = "column";
    }
}

function mostrarComidas3() {
    if (estC3 == false) {
        estC3 = true;
        SubS3.style.display = "flex";
        postres.style.width = "90%";
        bebidas.style.display = "none";
        comidas.style.display = "none";
    } else {
        estC3 = false;
        SubS3.style.display = "none";
        postres.style.width = "25%";
        bebidas.style.display = "flex";
        bebidas.style.flexDirection = "column";
        comidas.style.display = "flex";
        comidas.style.flexDirection = "column";
    }
}



class PH {
    constructor(pid) {
        this.p = document.getElementById(pid);
    }

    mostrar() {
        if (this.p.style.display == "flex") {
            this.p.style.display = "none";
        } else {
            this.p.style.display = "flex";
        }
    }
}

var ph_sn1 = new PH("p1");
var ph_nh = new PH("p2")
var ph_na = new PH("p3")
var ph_nc = new PH("p4")
var ph_nf = new PH("p5")
var ph_sn = new PH("p6")
var ph_co = new PH("p7")





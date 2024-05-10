let p1 = document.getElementById("p1");
let p2 = document.getElementById("p2");
let p3 = document.getElementById("p3");
let p4 = document.getElementById("p4");
let p5 = document.getElementById("p5");
let p6 = document.getElementById("p6");
let p7 = document.getElementById("p7");

let estf1 = false;
let estf2 = false;
let estf3 = false;
let estf4 = false;
let estf5 = false;
let estf6 = false;
let estf7 = false;

function mostrarTexto1(){
    if(estf1==false){
        estf1=true;
        p1.style.display="flex";
    } else {
        estf1=false;
        p1.style.display="none";
    }
}

function mostrarTexto2(){
    if(estf2==false){
        estf2=true;
        p2.style.display="flex";
    } else {
        estf2=false;
        p2.style.display="none";
    }
}

function mostrarTexto3(){
    if(estf3==false){
        estf3=true;
        p3.style.display="flex";
    } else {
        estf3=false;
        p3.style.display="none";
    }
}

function mostrarTexto4(){
    if(estf4==false){
        estf4=true;
        p4.style.display="flex";
    } else {
        estf4=false;
        p4.style.display="none";
    }
}

function mostrarTexto5(){
    if(estf5==false){
        estf5=true;
        p5.style.display="flex";
    } else {
        estf5=false;
        p5.style.display="none";
    }
}

function mostrarTexto6(){
    if(estf6==false){
        estf6=true;
        p6.style.display="flex";
    } else {
        estf6=false;
        p6.style.display="none";
    }
}

function mostrarTexto7(){
    if(estf7==false){
        estf7=true;
        p7.style.display="flex";
    } else {
        estf7=false;
        p7.style.display="none";
    }
}
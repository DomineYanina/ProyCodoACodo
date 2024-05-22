function ocultar_festejos() {
    lbl_festejos = document.getElementById("festejos");
    lbl_festejos.style.display = "none"
}

function mostrar_festejos() {

    lbl_festejos = document.getElementById("festejos");
    lbl_festejos.style.display = "flex"
}

class PH {
    constructor(pid) {
        this.p = document.getElementById(pid);
    }

    mostrar() {
        if (this.p.style.display == "flex") {
            this.p.style.display = "none";
            this.p.style.height = "110px";//Esto debería hacerse sobre el elemento de clase sector que corresponda según en cual estoy haciendo click, no sobre la p
            //Acá el elemento de clase sector que corresponda según el cual estoy haciendo click, debería volver a ajustarse para que vuelva al 25%
        } else {
            this.p.style.display = "flex";
            this.p.style.height = "fit-content"; //Esto debería hacerse sobre el elemento de clase sector que corresponda según en cual estoy haciendo click, no sobre la p
            //También sobre el elemento de clase sector que corresponda según el cual estoy haciendo click, debería ajustarsele el width para que pase a ser del 29%, en vez del 25%
            this.p.style.backgroundColor = rgba(140, 0, 0, 0);
        }
    }
}

class Platos {
    constructor(id_plato) {
        this.platos = [
            [document.getElementById("comidas"), document.getElementById("SubS1")],
            [document.getElementById("bebidas"), document.getElementById("SubS2")],
            [document.getElementById("postres"), document.getElementById("SubS3")]
        ];

        this.plato = document.getElementById(id_plato);
    }
    mostrar() {

        for (let plat of this.platos) {
            if (plat[0] === this.plato) {
                if (plat[0].style.width == "25%") {
                    plat[0].style.width = "95%";
                    plat[0].style.backgroundColor = "#4e00647a";
                    plat[0].style.color = "yellow";
                    plat[1].style.display = "flex";
                    for (let plat2 of this.platos) {
                        if (plat2[0] !== this.plato) {
                            plat2[0].style.display = "none"

                        }
                    }
                } else {
                    plat[0].style.width = "25%";
                    plat[0].style.backgroundColor = ""
                    plat[0].style.color = "";
                    plat[1].style.display = "none";
                    for (let plat2 of this.platos) {
                        if (plat2[0] !== this.plato) {
                            plat2[0].style.display = "flex"
                            plat2[0].style.flexDirection = "column"
                        }
                    }
                }

            }
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

var comm = new Platos("comidas")
var bebb = new Platos("bebidas")
var poss = new Platos("postres")

document.addEventListener('scroll', function() {
    const logo = document.querySelector('.logo');
    const threshold = 100;
    
    if ((window.innerHeight + window.scrollY) >= (document.body.offsetHeight - threshold)) {
    logo.classList.add('large');
    } else {
    logo.classList.remove('large');
    }
});
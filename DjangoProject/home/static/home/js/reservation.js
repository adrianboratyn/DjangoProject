function getPrice()
{
    console.log(1)
    
    var cena= parseInt(document.getElementById("price").innerText);
    var dorosli= parseInt(document.getElementById("dorosli").value);
    var dzieci=parseInt(document.getElementById("dzieci").value)
    var result= dorosli*cena+dzieci*(cena*0.75)
    console.log(result)

var przewodnik=document.getElementById("prywatny_przewodnik")
if(przewodnik.checked)  
    result += 300
var pokoj=document.getElementById("pokoj")
if(pokoj.checked)
    result += 400

var out=document.getElementById("out")


out.innerText = result
}


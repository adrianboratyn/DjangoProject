    var userk = document.getElementById("k2").textContent
    var tripk = document.getElementById("k1").value
    var tripkid = document.getElementById("k4").textContent
    var user = document.getElementById("id_user")
    var trip = document.getElementById("id_trip")
    var termink = document.getElementById("termin")
    var termin = document.getElementById("id_day")
    var cenak= document.getElementById("k3").textContent
    var dorosli = document.getElementById("id_adults")
    var dzieci = document.getElementById("id_kids")
    var cena = document.getElementById("id_price")
    var przewodnik = document.getElementById("id_guide")
    var pokoj = document.getElementById("id_room")

    dorosli.oninput = getPrice;
    dzieci.oninput = getPrice;
    przewodnik.oninput = getPrice;
    pokoj.oninput = getPrice;
    termink.onchange = getPrice;

getPrice();
function getPrice()
{
    user.selectedIndex=parseInt(userk)-1;
    trip.selectedIndex=tripkid-1

    termin.value=termink.options[termink.selectedIndex].value
    var result= parseInt(dorosli.value)*cenak+(parseInt(dzieci.value)*(cenak*0.75))

    if(przewodnik.checked)  
        result += 300

    if(pokoj.checked)
        result += 400
    
        cena.value=result

    var out=document.getElementById("out")

    out.innerText = result
}

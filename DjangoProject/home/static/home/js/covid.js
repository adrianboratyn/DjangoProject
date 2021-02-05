active = document.getElementById("active")
date = document.getElementById("date")
var country=document.getElementById("country").textContent
function getPosts() {
    fetch(`https://api.covid19api.com/live/country/${country}/status/confirmed`)
    .then((respond) => respond.json())
    .then((data) => {
        obj = data.pop();
        active.innerText = obj.Active
        date.innerText=obj.Date.substring(0,10);
    })
    .catch((error) => console.log(error));
}
getPosts()
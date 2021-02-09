var z = {Ponta_Delgada: "37d74n25d68/ponta-delgada/",
         Dominican_Republic: "18d74n70d16/dominican-republic/"}

var pogoda = document.getElementById('pogoda')
pogoda.href += z[pogoda.getAttribute('data-label_1')] 

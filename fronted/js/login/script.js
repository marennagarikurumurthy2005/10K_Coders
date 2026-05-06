let data=document.getElementById('inp2')
let btnd=document.getElementById('btn')

btnd.addEventListener("click",sh)

function sh(){
    if (btnd.textContent=="show"){
    data.type="text"
    btnd.textContent="hide"
}
else{
    data.type="password"
    btnd.textContent="show"
}
}



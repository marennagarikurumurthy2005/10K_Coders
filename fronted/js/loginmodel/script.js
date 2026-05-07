let form=document.getElementById('form')
let openb=document.getElementById('openb')
let b=document.getElementsByClassName('mainwrapper')






form.style.transitionDuration="1s"

function openclose() {

    if (openb.textContent=="open")
    {

        form.style.marginTop="50px"
        openb.textContent="close"

    }

    else{
        form.style.marginTop="-1000px"
        openb.textContent="open"

    }
    
    
    
}

openb.addEventListener("click",openclose)




let display=document.getElementById('display')
let btn=document.getElementById("btn")


// age=agedata.textContent


btn.addEventListener("click",()=>{
    let age=document.getElementById("age").value
    
    let promise=new Promise((resolve, reject) => {
        
        if (age>18){
            resolve("Eligible")
        }
        else{
            reject("Not eligible")
        }
    })

    promise
        .then((msg)=>{
            
            setTimeout(() => {
                display.textContent=msg
            }, 1000);
        })
        .catch((err)=>{
            setTimeout(() => {
                display.textContent=err
            }, 1000);
        })

})

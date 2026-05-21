
let display=document.getElementById('display')
let agedata=document.getElementById("age")
let btn=document.getElementById("btn")



// age=agedata.textContent


btn.addEventListener("click",()=>{
    console.log(agedata)
    age=agedata.innerText
    console.log(age);
    

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

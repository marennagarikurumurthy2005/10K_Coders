

function demo(a,b){
    return new Promise((resolve, reject) => {
        if (isNaN(a) || isNaN(b)){
            reject("invalid inputs")
        }
        else{
            resolve([a,b])
        }
    })

}

let call=demo(10,20)

call
    .then((msg)=>{
        for(let i=msg[0];i<=msg[1];i++){
            console.log(i);
            
        }
    })
    .catch((err)=>{
        console.log(err);
        
    })
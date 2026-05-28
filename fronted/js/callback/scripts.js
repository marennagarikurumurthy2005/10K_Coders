// function register(login){
//     setTimeout(() => {
//         console.log("registered");
//         login(dashboard)
//     }, 5000);
// }

// function login(dashboard){
//     setTimeout(() => {
//         console.log("Login");
//         dashboard(payment)
//     }, 4000);
// }

// function dashboard(payment){
//     setTimeout(() => {
//         console.log("dashboard");
//         payment(order)
//     }, 3000);
// }

// function payment(order){
//     setTimeout(() => {
//         console.log("Payment done");
//         order()
//     }, 2000);
// }

// function order(){
//     setTimeout(() => {
//         console.log("order placed");
        
//     }, 1000);
// }

// register(login)



// using promie chaining

function greenCart(str){
    return new Promise((resolve, reject) => {
        if (str){
            resolve("successfully")
        } else reject("Invalid credits")
    })

}

user=greenCart(true)

user
    .then((res)=>{
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                console.log("registered",res);

                resolve(res)
                
            }, 1000);
            
        })
    })
    .then((res)=>{

        return new Promise((resolve, reject) => {
            setTimeout(() => {
                console.log("Login",res);

                resolve(res)
                
            }, 1000);
        })

    })
    .then((res)=>{
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                console.log("Dashboard");
                resolve(res)
                
            }, 1000);
        })
    })
    .then((res)=>{
        return new Promise((resolve,reject)=>{
            setTimeout(()=>{
                    console.log("Payment completed",res)
                    resolve(res)
            },1000);
        })
    })
    .then((res)=>{
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                console.log("orded placed",res);
                
            }, 1000);
        })
    })
    .catch((rej)=>{
        console.log(rej);
        
    })
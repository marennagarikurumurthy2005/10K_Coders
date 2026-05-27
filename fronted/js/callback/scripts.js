function register(login){
    setTimeout(() => {
        console.log("registered");
        login(dashboard)
    }, 5000);
}

function login(dashboard){
    setTimeout(() => {
        console.log("Login");
        dashboard(payment)
    }, 4000);
}

function dashboard(payment){
    setTimeout(() => {
        console.log("dashboard");
        payment(order)
    }, 3000);
}

function payment(order){
    setTimeout(() => {
        console.log("Payment done");
        order()
    }, 2000);
}

function order(){
    setTimeout(() => {
        console.log("order placed");
        
    }, 1000);
}

register(login)
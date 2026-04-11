//  named functions

function learn(){
    console.log("Named functions")
}
learn()

// genrator functions * yield 
 function * genrator(){
    
    yield 1
    yield 2
    yield 3

}

let a=genrator()
console.log(a.next());



//  anonymus function => no name

const x=function(){
    console.log("This is anonymous function")
}

x()

//  Arrow functions 

const data=()=>{
    console.log("This is arrow function")
}
//  this keyword

let b=40
const net=()=>{
let b=10
console.log(b);

}

net()

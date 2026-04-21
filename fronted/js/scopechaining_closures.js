//  scope chaining is nothing but binding of variable of parent and iunnermost element 
//  there are 3 types of scopes in js 

//  block scope :- the variables declared and used inside the inner most block the child variables cannot accesses by parent
//  local scope :- the variables declared inside the parent , can be accessed into child classes 

//  global scope :- the var from window object and can be accessed anywhere

// example


/* var a =2 // global level can access anywhere
function parent(){
    let a =1 // local level can access in parent and its child but not outside parent
    function child(){
        let a=0 // block level can access only in this block
        console.log(a);
        // console.log(this.a);  this is used to call the global element by crossing the local scope
         
    }
} */


//  closures

// closure is the bind between parent and inner most elements and also stored the values of the parents and globals
// const parent=()=>{
//     let a=10
//     const child=()=>{
//         console.log(a)
//         return "closures in js"
//     }
//     return child;
// }
// calling=parent()
// console.log(calling());


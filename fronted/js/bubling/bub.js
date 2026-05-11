let gp=document.querySelector('#gp')
let p=document.getElementById('p')
let c=document.getElementById('c')
let main=document.querySelector('.mainwrapper')


// bubbling is event calling from bottom to top to stop it we use stoppropagation with any aurguments
gp.addEventListener('click',()=>{

    console.log("gp");
    
})
p.addEventListener('click',()=>{
    console.log("p");
    
})

c.addEventListener('click',()=>{
    console.log("c");
})


// capturing is calling events from top to bottom just add "true" at end 
gp.addEventListener('click',()=>{

    console.log("gp");
    
},true)
p.addEventListener('click',()=>{
    console.log("p");
    
},true)

c.addEventListener('click',()=>{
    console.log("c");
    
},true)

// gp.addEventListener('click',(e)=>{
//     e.stopPropagation()
//     console.log("gp");
    
// })
// p.addEventListener('click',(e)=>{
//     e.stopPropagation()
//     console.log("p");
    
// })

// c.addEventListener('click',(e)=>{
//     e.stopImmediatePropagation()
//     console.log("c");
    
// })


// event deligation == instead of writing stop propogation get id by elements and then based on id add event conditions

// main.addEventListener('click',(e)=>{

//     console.log(e.target)
//     if (e.target.id=="c"){
//         c.style.backgroundColor="purple"
//     }
//     if (e.target.id=="p"){
//         p.style.backgroundColor="orange"
//     }
//     if (e.target.id=="gp"){
//         gp.style.backgroundColor="blue"
//     }
    


// })

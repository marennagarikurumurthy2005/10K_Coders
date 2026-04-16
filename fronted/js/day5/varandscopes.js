

//  types of variables let var  const


// console.log(a)
// let a=0
// console.log(a);

// console.log(b)
// var b=1
// console.log(b);

// console.log(c)
// const c=2
// console.log(c);


// let a
// a=10
// console.log(a);


// let a=10
// // a=20
// // let a=20
// console.log(a);


// var a=10
// // a=20
// var a =20
// console.log(a);



// const a=0
// // a=10 not possible

// console.log(a);





//  callback functions


// const a =(calling)=>{
//     console.log("This is main function");
//     calling()
// }
// function calling(){
//     console.log("this is a callback function");
// }
// a(calling)



const available=(current,deposite,calling)=>{
    console.log(current+deposite);
    
    calling()

}

const transaction_status=_=>{
    console.log("Deposite successfull");
}

available(1500,400,transaction_status)


















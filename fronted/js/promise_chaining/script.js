// function demo(a,b){

//     return new Promise((resolve, reject) => {
//         if (isNaN(a) || isNaN(b)){
//             reject("Invalid numbers")
//         }
//         else{
//             resolve([a,b])
//         }
//     })

// }

// let call=demo(1,10)

// call
//     .then((msg)=>{
//         console.log(msg);
//     })
//     .catch((err)=>{
//         console.log(err);
//     })

//  promise chaining

// function demo(str){
//     return new Promise((resolve, reject) => {

//     if (str==1) {
//         resolve()
//     } else {
//         reject()

//     }

//     })
// }

// prom=demo(1)

// prom
//     .then((msg)=>{
//         setTimeout(()=>{
//             console.log("Register");
//         },3000)
//         return msg
//     })
//     .then((msg)=>{
//         setTimeout(() => {
//     console.log("login");

//     }, 2000);
//     return msg

//     })
//     .then((msg)=>{
//         setTimeout(() => {
//             console.log("Dashboard");

//         }, 1000);
//     })
//     .catch((err)=>{
//         console.log("Invalid Credits");

//     })

function demo(res) {
  return new Promise((resolve, reject) => {
    if (res == 1) {
      resolve("success");
    } else reject("invalid credits");
  });
}

prom = demo(1);

prom
  .then((msg) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        console.log("registered");
        console.log(msg);
        resolve(msg);
      }, 3000);
    });
  })
  .then((msg) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        console.log("Logged in");
        console.log(msg);
        resolve(msg);
      }, 2000);
    });
  })
  .then((msg) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        console.log("Dashboard");
        console.log(msg);
        resolve(msg);
      }, 1000);
    });
  })
  .catch((err) => {
    console.log(err);
  });

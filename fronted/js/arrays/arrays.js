// creating array in 3 ways
// 1 way literals

// let arr=[1,2,3,4,5,6]
// console.log(arr);

// by using array() constructor

// let arr=Array(1,2,3,4,5,6)
// console.log(arr);


// using new keyword

// let arr=new Array(1,2,3,4,5)
// console.log(arr);



// 3 sum

let arr=[1,0,-1,2,0,1,-1]
let target=1

for (let i=0;i<=arr.length-1;i++){
    for(let j=i+1;j<=arr.length-1;j++){
        for(let k=j+1;k<=arr.length-1;k++)
            if (arr[i]+arr[j]+arr[k]==target){
                console.log(arr[i],arr[j],arr[k]);
            }
                

    }
}







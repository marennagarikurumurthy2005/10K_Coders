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

// let arr=[1,0,-1,2,0,1,-1]
// let target=1

// for (let i=0;i<=arr.length-1;i++){
//     for(let j=i+1;j<=arr.length-1;j++){
//         for(let k=j+1;k<=arr.length-1;k++)
//             if (arr[i]+arr[j]+arr[k]==target){
//                 console.log(arr[i],arr[j],arr[k]);
//             }
                

//     }
// }


// array methods
let arr=[1,2]
console.log(arr.lastIndexOf(2));
arr.push(10,20,30,40)
arr.pop()
arr.unshift(40)
arr.shift()
console.log((arr));

console.log((arr.slice(0,2)));

console.log(arr.splice(3,2,7,6,9));

console.log(arr);









//  push -- add elements to arr at end
//  pop -- delete elements from end
// unshift --add elements from start
// shift -- delete elements from the start
// splice -- used to delete the sub part of arr and cxan add elements if need
// slice -- to extract the sub array from original array
// concate --used to add 2 or more arrays arr1.concat(arr2,3,4,etc)
// at  --it accepts the negative indexing of array
// lastindexof -- returns the index for  element to searh from end else -1
// find index --same but searvches from right 
// join -- used to join the list elements with seperator
// lengh -- returns the len of arr 





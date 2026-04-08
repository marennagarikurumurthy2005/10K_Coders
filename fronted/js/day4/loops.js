// count the number of digit in a number
// let num=123
// let num_sum=0
// let count=0
// while (num>0){
//     rem=num%10
//     count++
//     num_sum=num_sum+rem
//     num=Math.floor(num/10)
// }

// console.log((num_sum));
// console.log(count);

//  reversing a given number 

// let num=123
// let newnum=0
// while (num>0){
//     rem=num%10
//     newnum=newnum*10+rem
//     num=Math.floor(num/10)

// }
// console.log(newnum);

// const num=10
// if (num>0){
//     console.log("positive");
    
// }
// else if  (num<0) {
//     console.log("negative");
    
    
// } 
// else {
//     console.log("zero");
    
// }



// let num=4586
// let max=0
// while (num>0){
//     rem=num%10
//     if (rem>max){

//         max=rem

//     }
//     num=Math.floor(num/10)
// }
// console.log(max);


let num=12321
let temp=num
let newnum=0
while (num>0){
    rem=num%10
    newnum=newnum*10+rem
    num=Math.floor(num/10)

}
if (temp==newnum){
    console.log("yes palindrome")
}
else{
    console.log("Not a palindrome");
    
}












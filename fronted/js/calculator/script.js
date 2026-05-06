let input=document.getElementById('inp')

function display(value){

    input.value+=value

};

function calculate(){
    input.value=eval(input.value)
}

function clearAll(){
    input.value=""

}
function deleteLast(){
    data=input.value
    data=data.slice(0,-1)
    input.value=data
}

let vid=document.querySelector('.vid')
let ads=document.querySelector('.ads')
let colors=["blue","red","purple","pink","peach"]
let count=0
setInterval(() => {
    ads.style.display="block"
    ads.style.backgroundColor=colors[count]
    vid.pause();
    count++

    if (count>=colors.length){
        count=0
    }

    setTimeout(() => {
        ads.style.display="none"
        vid.play();
    }, 2000);
}, 10000);
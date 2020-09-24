let time=600;
setInterval (myFunction,1000)
const countdown=document.getElementById("mins");
function myFunction() {
    const mins=Math.floor(time/60);
    countdown.innerHTML()=mins;
    time--;
}
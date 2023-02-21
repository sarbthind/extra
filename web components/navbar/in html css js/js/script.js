const menu = document.querySelector('.menu')
const exit = document.querySelector('.exit')
const navbar = document.querySelector('.navbar')
exit.style.display="none"
const meenu = ()=>{
    if(exit.style.display=="none"){
        exit.style.display="block"
        navbar.style.display='block'
        menu.style.display="none"
    }
    else{
        exit.style.display="none"
        menu.style.display="block"
        navbar.style.display='none'
    }
}
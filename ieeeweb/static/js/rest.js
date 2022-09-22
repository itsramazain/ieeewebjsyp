const ham=document.querySelector('.ham')
const nav=document.querySelector('.items')
ham.addEventListener('click',() => {
    ham.classList.toggle('active')
    nav.classList.toggle('active')
})
document.querySelectorAll('.item-link').forEach(n => n.addEventListener('click', ()=> {
    ham.classList.remove('active')
    nav.classList.remove('active')
    
 }))
 
 var background=document.querySelector('.slider')
 var rest=document.querySelector('.place')
 var btn=document.querySelector('.joinBtn')
 window.addEventListener('scroll',function(){
    var value=window.scrollY
    
    background.style.height=35-0.15*value+'vh'
    rest.style.top=215-value+'px'
    console.log(value+' value')
    console.log(background.style.height+' pic')
    console.log(rest.style.top+' text')
    
    
 })
 
 var arrow1=document.querySelectorAll('.fa-caret-down')[0]
 var sub1=document.querySelectorAll('.subitems')[0]
    arrow1.addEventListener('click', ()=> {
        sub1.classList.toggle('active')
    })
 var arrow2=document.querySelectorAll('.fa-caret-down')[1]
 var sub2=document.querySelectorAll('.subitems')[1]
    arrow2.addEventListener('click', ()=> {
        sub2.classList.toggle('active')
    })
 var arrow3=document.querySelectorAll('.fa-caret-down')[2]
 var sub3=document.querySelectorAll('.subitems')[2]
    arrow3.addEventListener('click', ()=> {
        sub3.classList.toggle('active')
    })
var arrow4=document.querySelectorAll('.fa-caret-down')[4]
var sub4=document.querySelectorAll('.subitems')[3]
    arrow4.addEventListener('click', ()=> {
        sub4.classList.toggle('active')
     })
var arrow5=document.querySelectorAll('.fa-caret-down')[3]
var sub5=document.querySelectorAll('.subsubitems')[0]
    arrow5.addEventListener('click', ()=> {
        sub5.classList.toggle('active')
     })







    
    
    
document.querySelectorAll('.sublink').forEach(n => n.addEventListener('click', ()=> {
   for(var i=1;i<subs.length;i++){
   subs[i].classList.remove('active')
}
    
    
 }))





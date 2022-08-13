const contImage = document.querySelector('.cont-image')
const showImageIMG = document.querySelector('.show-image')
const allImages = document.querySelectorAll('.img')

allImages.forEach(image =>{
    image.addEventListener('click',()=>{
        
        addImageLightbox(image.getAttribute('src'))
    })
})

const addImageLightbox = (src)=>{
    
    contImage.classList.toggle('move')
    showImageIMG.src = src
}
contImage.addEventListener('click',()=>{
    contImage.classList.toggle('move')
})
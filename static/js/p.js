// var btn_cart = document.querySelector('.btn_cart');
// btn_cart.addEventListener('click',function(event){
//     if(event.target.hasAttribute('data-book-id')){
//         const card=event.target.closest('.box-book');
//         console.log(card)

//     }

// })

$(document).ready(function() {
    $(".btn_cart").click(function(event) {
        let productInfo={};
        event.preventDefault();
        let existingCartBookID = localStorage.getItems("productInfo")

 
        
        if(event.target.hasAttribute('data-book-id')){
            
            const card=event.target.closest('.box-book');
            let bookID = event.target.attributes['data-book-id'].value
            productInfo={
                id:bookID,
                imgSrc:card.querySelector('.bookimg').attr('src'),
                title:card.querySelector('.booktitle').innerText,
                cost:card.querySelector('.bookcost').innerText,
                count:1
            }
    
        }
    }
    })
})
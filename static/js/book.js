var btn_cart = document.querySelector('.btn_cart');

btn_cart.addEventListener("click",  function(event) {
    // event - делегат события    
    event.preventDefault();

    let bookID = event.target.attributes['data-book-id'].value

        let book=event.target.closest('.box-book');
        let items = 
            {
                "id":bookID;
                "name": book.querySelector('.booktitle'),
                "count": 1
            };
         

        localStorage.setItem("items", obj)

        let bookSection = document.querySelector('.book-section-' + bookID)

        bookSection.innerHTML += `
            <a href="#" class="remove_from_cart">Убрать из корзины</a>
        `
    
})
let name = $.data(parsedItems, "name");
let img = $.data(parsedItems, "img");
let quantity = $.data(parsedItems, "quantity");
let price = $.data(parsedItems, "price");

console.log(name,price,img,quantity)

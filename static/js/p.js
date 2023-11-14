
$(document).ready(function() {
    $(".btn_cart").click(function(event) {
        event.preventDefault();
        let bookID = event.target.attributes['data-book-id'].value
        let bookContainer = $(".book-section-" + bookID);
        let bookName = bookContainer.find(".booktitle").text()
        let bookImage = bookContainer.find(".bookimg").attr('src')
        let bookCost = bookContainer.find(".bookcost").attr('data-cost')
     
        let cartItems = JSON.parse(localStorage.getItem("cartItems"))
       
        if (cartItems !== null){
            let bookInCartPredicate = book => book.id === bookID;

            let bookInCartExists = cartItems.some(bookInCartPredicate)

            if (bookInCartExists) {
                cartItems.forEach(element => {
                    if (element.id === bookID) {
                        element.quantity += 1
                    }
                });
            }
            else {
                cartItems.push(
                    {
                        "id": bookID,
                        "name": bookName,
                        "img": bookImage,
                        "price": bookCost,
                        "quantity": 1
                    }
                )
            }
            localStorage.setItem("cartItems", JSON.stringify(cartItems))
        }
        else {
            localStorage.setItem("cartItems", JSON.stringify([
                {
                    "id": bookID,
                    "name": bookName,
                    "img": bookImage,
                    "price": bookCost,
                    "quantity": 1
                }
            ]))
        }

    })
})
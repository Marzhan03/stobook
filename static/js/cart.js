let cartItems
let cart=``
let quantity
function loadCart(){
    
    if (this.localStorage.getItem("cartItems")){
        cartItems = JSON.parse(localStorage.getItem("cartItems"));
        let sumItems=0
        $.each(cartItems, function(index, item) {
            let ind=index;
            let id=item.id;
            let img=item.img;
            let name = item.name;
            let price = parseInt(item.price);
            quantity = item.quantity;
            let sum = quantity*price
            sumItems=sumItems+sum
            cart=`
                <div><img class="basket-img" src="${ img }"></div>
                    <div class="name"><h4>${name}</h4></div>
                    <div class="price" ><h4>${price}</h4></div>
                    <div class="items-counter-wrapper" data-counter>
                    <a href="#" class="items__control" id="minus-btn" data-id="${id}" >-</a>
                       
                        <div class="items__current" data-counter data-id="${id}">${quantity}</div>
                   
                        <a href="#" class="items__control" id="plus-btn" data-id="${id}">+</a>
                    </div>
                    <div class="sum">${sum}</h4></div>
                    <input class="delete-all" id="delete-item" data-ind="${ind}" type="button" value="Очистить"></input>
            
                `
         
                $('.basket-item').append(cart);
    
        });
            let sumItem=`
                <div><h3>Итоговая сумма:</h3></div>
                <div><h3>${ sumItems }</h3></div>` 
            $('.basket-sum').append(sumItem)  
    }
    else{
        cart=`<h2 class="empty">Корзина пуста</h2>`
        $('.basket-items-container').append(cart);

    }
 
    $(".basket-items-container").on('click', '#delete-item', delItem);

    // $('#delete-item').on('click',delItem);
    $(".basket-title").on('click','#delete-all-items',delAllItem);
    $(".items-counter-wrapper").on('click','#minus-btn',minusBtn);
    $(".items-counter-wrapper").on('click','#plus-btn', function(event) {

        let id =parseInt($(this).attr('data-id'));
        cartItems = JSON.parse(localStorage.getItem("cartItems"));
        $.each(cartItems, function(index, item) {
            if (id==item.id){
                item.quantity+=1
                saveItem()
                 
            }
        });
    });
}


function delItem(){
    let id =parseInt($(this).attr('data-ind'));
    cartItems.splice(id,1);
    saveItem()
}

 function delAllItem(){
     cartItems=[]
     saveItem()
     cart=`<h2 class="empty">Корзина пуста</h2>`
         $('.basket-items-container').append(cart);
   
 }

 function minusBtn(){
    let id =parseInt($(this).attr('data-id'));
  
    cartItems = JSON.parse(localStorage.getItem("cartItems"));
    $.each(cartItems, function(index, item) {
        if (id==item.id){
            if (item.quantity==1){
                console.log("dfsfs")
                console.log(cartItems)
                cartItems.splice(index,1);
                saveItem()
            }
            else {
                item.quantity-=1
                saveItem()   
            }    
        }
    });
 }


function saveItem(){
    location.reload()
    localStorage.setItem('cartItems',JSON.stringify(cartItems));
   
    }

$(document).ready(function() {
    loadCart();
});

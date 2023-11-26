let cartItems
let cart=``
let quantity
let sumItems =0;
function loadCart () {
    if (this.localStorage.getItem("cartItems")){
        cartItems = JSON.parse(localStorage.getItem("cartItems"));
        var sumItems = 0;

        $.each(cartItems, function(index, item) {
            let price = parseInt(item.price);
            let quantity = item.quantity;
            let sum = quantity * price;
            sumItems = sumItems + sum;

            cart=`
                <div class="item_container_${item.id}" id="item-container">
                    <div><img class="basket-img" src="${item.img}"></div>
                    <div class="name"><h4>${item.name}</h4></div>
                    <div class="price" ><h4>${price}</h4></div>
                    <div class="items-counter-wrapper" data-counter>
                        <a href="#" class="items__control" id="minus-btn" data-id="${item.id}" >-</a>
                        <div id="cart_item__div_${item.id}" class="items__current" data-counter data-id="${item.id}">${quantity}</div>
                        <a href="#" class="items__control" id="plus-btn" data-id="${item.id}">+</a>
                    </div>
                    <div id="item_sum_${item.id}" class="sum">${sum}</h4></div>
                    <input class="delete-all" id="delete-item" data-ind="${index}" data_book_id="${ item.id }" type="button" value="Удалить"></input>
                </div>
                `

            $('.basket-item').append(cart);
    
        });

        totalsum = JSON.parse(localStorage.getItem("totalsum"));
        totalsum.allsum=sumItems
        saveItem("totalsum", totalsum)
            let sumItem=`
                <div><h3>Итоговая сумма:</h3></div>
                <div id="all_items"><h3>${ sumItems }</h3></div>` 
            $('.basket-sum').append(sumItem)  
        
    }
    else{
        cart=`<h2 class="empty">Корзина пуста</h2>`
        $('.basket-items-container').append(cart);

    }
 
    $(".basket-items-container").on('click', '#delete-item', delItem);
    $(".basket-title").on('click','#delete-all-items',delAllItem);
    $(".items-counter-wrapper").on('click','#minus-btn',minusBtn);
    $(".items-counter-wrapper").on('click','#plus-btn', function(event) {
        event.preventDefault();
        let id =parseInt($(this).attr('data-id'));
        cartItems = JSON.parse(localStorage.getItem("cartItems"));
        $.each(cartItems, function(index, item) {
            if (id==item.id){
                item.quantity+=1;
                saveItem("cartItems",cartItems);
                item_sum=item.quantity*item.price;
                let current_item_div = $(`#cart_item__div_${item.id}`)
                current_item_div.text(item.quantity)
                let current_item_sum = $(`#item_sum_${item.id}`)
                current_item_sum.text(item_sum)
                let current_item_all_sum = $(`#all_items`)
                totalsum = JSON.parse(localStorage.getItem("totalsum"));
                let allSum=parseInt(totalsum.allsum)
                allSum+= parseInt(item.price)
                totalsum.allsum=allSum
                saveItem("totalsum",totalsum)
                current_item_all_sum.text(allSum)

            }
        });
    });
}


function delItem(){
    event.preventDefault();
    let id =parseInt($(this).attr('data-id'));
    let data_book_id=parseInt($(this).attr('data_book_id'));
    cartItems.splice(id,1);
    saveItem("cartItems",cartItems)       
    $.each(cartItems, function(index, item) {
        
        if (parseInt(item.id) == data_book_id){
      
            $('.item_container_' + item.id).remove(); 
            totalsum = JSON.parse(localStorage.getItem("totalsum"));
                let allSum=parseInt(totalsum.allsum)
                c= parseInt(item.price)*parseInt(item.quantity)
                allSum=allSum-c
                let current_item_all_sum = $(`#all_items`)
                totalsum.allsum=allSum
                saveItem("totalsum",totalsum)
                
                current_item_all_sum.text(allSum)
        
        }
    });
}

function delAllItem(){
    event.preventDefault();
    cartItems=[]
    saveItem("cartItems",cartItems)
    $('.basket-item').remove(); 
    cart=`<h2 class="empty">Корзина пуста</h2>`
        $('.basket-items-container').append(cart);
}

function minusBtn(event) {
    event.preventDefault();
    let id =parseInt($(this).attr('data-id'));
    cartItems = JSON.parse(localStorage.getItem("cartItems"));
    
    $.each(cartItems, function(index, item) {
        if (id==item.id){
            if (item.quantity==1){
                cartItems.splice(index, 1);
                saveItem("cartItems",cartItems)
                $('.item_container_' + item.id).remove();
            }
            else {
                item.quantity-=1
                saveItem("cartItems",cartItems) 
                item_sum=item.quantity*item.price;
                let current_item_div = $(`#cart_item__div_${item.id}`)
                let current_item_sum = $(`#item_sum_${item.id}`)
                let current_item_all_sum = $(`#all_items`)
                current_item_div.text(item.quantity)  
                current_item_sum.text(item_sum) 
                console.log(current_item_all_sum,"dsfd",sumItems)
                totalsum = JSON.parse(localStorage.getItem("totalsum"));
                let allSum=parseInt(totalsum.allsum)
                allSum-= parseInt(item.price)
                totalsum.allsum=allSum
                saveItem("totalsum",totalsum)
                
                // current_item_all_sum.text(allSum)
            }    
        }
    });
 }


function saveItem(itemName, itemValue){
    localStorage.setItem(itemName, JSON.stringify(itemValue));
   
    }

$(document).ready(function() {
    loadCart();
    let totalsum = JSON.parse(localStorage.getItem("totalsum"))
    // let bookContainer = $('.basket-sum').text(totalSum);
    
});

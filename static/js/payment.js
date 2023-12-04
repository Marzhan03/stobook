function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Находим CSRF-токен в куке
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    let totalsum = JSON.parse(localStorage.getItem("totalsum"));
    console.log(totalsum)
    totalsum = totalsum['allsum']; 
    console.log(totalsum)
    let delivery=500
    var totalSumma=delivery+parseInt(totalsum)
    summa=`<h3>Информация об оплате</h3>
    <h4>Стоимость товаров: ${totalsum} ₸</h4>
    <h4>Стоимость доставки: ${delivery}</h4>
    <br><h4>Итого: ${totalSumma}</h4>`
    $('.order-info').append(summa);
    var csrftoken = getCookie('csrftoken'); // Получаем CSRF-токен
    $.ajax({
        url:"http://localhost:8000/get_user_orders",
        type: "GET",
        success: function(order){
            let orderSelect = $("#order");
            order.forEach((element) =>{
                orderSelect.append(`
                <h3>Информация о доставке</h3>
                <h4>${element.customer_user.last_name} ${element.customer_user.first_name}</h4>
                <h4>Адрес доставки: 
                    город ${element.to_address.streetname.city.city},
                    улица ${element.to_address.streetname.street},
                    дом ${element.to_address.housenumber},
                    квартира ${element.to_address.flatnumber}
                </h4>
                <h4>Номер телефона: ${element.customer_user.phone_number}<h4>
                <h4>email: ${element.customer_user.email}<h4>	
                <h4>Способ доставки: KazPost</h4>
                    `)
            })
        }
    })
    
    $("#openBtn").click(function(){
        let orderId=$("#orderId").val()
        let cardnumber=$("#numberCard").val()
        let dateissue=$("#month").val()+$("#year").val()
        let cvc=$("#ccv").val()
        let cardtype=$("#type").val()
     
        $.ajax({
            url:"http://localhost:8000/orders/payments/new",
            type: "POST",
            headers: {
                'X-CSRFToken': csrftoken // Добавляем CSRF-токен в заголовок запроса
            },
            data:{
                "order":orderId,
                "summa":totalSumma,
                "cardnumber":cardnumber,
                "dateissue":dateissue,
                "cvc":cvc,
                "cardtype":cardtype,
            },
            
            success: function(order){
               debugger


            }
            })

        // cartItems = localStorage.removeItem("cartItems")
        // totalsum = localStorage.removeItem("totalsum")
        $("#myModal").css("display", "block");
       

    });

    $(".close").click(function(){
        $("#myModal").css("display", "none");
    });

    $(window).click(function(event) {
        if (event.target == $("#myModal")[0]) {
            $("#myModal").css("display", "none");
        }
    });
});
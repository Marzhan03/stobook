$(document).ready(function() {
    // $.ajax({
    //     url: "http://localhost:8000/card_types",
    //     type: "GET",
    //     success: function(response) {
    //         let cardTypesSelect = $("#cardTypes");

    //         for (let index = 0; index < response.length; index++) {
    //             const element = response[index];

    //             cardTypesSelect.append(`
    //                 <option>${element.cardtypename}</option>
    //             `)
    //         }
    //     }

    // })

    $.ajax({
        url:"http://localhost:8000/cities",
        type: "GET",
        success: function(cities){
            let citiesSelect = $("#cities");
            cities.forEach((element) =>{
                citiesSelect.append(`
                    <option value="${element.id}">${element.city}</option>
                    `)
            })
        }
    })

    $("#cities").change(function(e){
        let city_id = $(this).find(":selected").val()
        $.ajax({
            url:"http://localhost:8000/streets/" + city_id,
            type: "GET",
            success: function(streets){
                let citiesSelect = $("#streets");
                citiesSelect.html('')
                streets.forEach((element) =>{
                    citiesSelect.append(`
                        <option value="${element.id}">${element.street}</option>
                        `)
                })
            }
        })
    });
    

    $("#orderBtn").click((event) => {
        event.preventDefault();

        var formData = $('form#order_form').serializeArray();

        let totalsum = JSON.parse(localStorage.getItem("totalsum"));
        let cartItems = JSON.parse(localStorage.getItem("cartItems"));

        let totalsumInput = $('<input>')
            .attr('type', 'hidden')
            .attr('name', 'totalsum')
            .val(totalsum);

        let booksInput = $('<input>')
            .attr('type', 'hidden')
            .attr('name', 'books')
            .val(JSON.stringify(cartItems));

        $('form#order_form').append(totalsumInput).append(booksInput);

        $('form#order_form').submit();

        cartItems = localStorage.removeItem("cartItems")
    })
})

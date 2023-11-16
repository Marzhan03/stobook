$(document).ready(function() {
    let baseUrl = "http://localhost:8000";

    $.ajax({
        url: baseUrl + "/card_types",
        type: "GET",
        success: function(response) {
            let cardTypesSelect = $("#cardTypes");

            for (let index = 0; index < response.length; index++) {
                const element = response[index];

                cardTypesSelect.append(`
                    <option>${element.cardtypename}</option>
                `)
            }
        }

    })

    $.ajax({
        url: baseUrl + "/cities",
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
            url: baseUrl + "/streets/" + city_id,
            type: "GET",
            success: function(streets){
                let citiesSelect = $("#streets");
                citiesSelect.html('')
                streets.forEach((element) =>{
                    citiesSelect.append(`
                        <option>${element.street}</option>
                        `)
                })
            }
        })
    });
    

    $("#orderBtn").click((event) => {
        let cartData = localStorage.getItem('cartItems');

        $.ajax({
            url: baseUrl + "/order",
            type: "POST",
            contentType: 'application/json',
            data: JSON.stringify(cartData),

            success: function(response) {
                debugger;
            },
            error: function(response) {
                debugger;
            }
        });
    })
})
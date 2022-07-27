
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


$(document).ready(function () {
    $(".add").click(function () {
        pro_id = Number($(this).attr("data-id"));
        qty = Number($(`input[name=quantity${pro_id}]`).val());
        //max quantity 10 minimum quantity 1
        if (qty >= 10) {
            qty = 10;
        } else if (qty <= 0 || qty ==NaN) {
            qty = 1;
        }
        console.log("ID: " + pro_id + ", Quantity: " + qty);
        $.ajax({
            type: "GET",
            url: "/cart/add",
            data: {
                "pro_id": JSON.stringify(pro_id),
                "pro_qty": JSON.stringify(qty),
            },
        })
    });

    $('.btn-remove').click(function () {
        pro_id = Number($(this).attr("data-id"));        
        $(`#pro${pro_id}`).remove();

        $.ajax({
            type: "GET",
            url: "/cart/remove",
            data: {
                "pro_id": JSON.stringify(pro_id),
            },
            success: function(){
                window.location.reload();
            }
        })
    });
/*
    $("#make-purchase").click(function () {
        let cost = Number(document.getElementById('total').textContent);
        $.ajax({
            type: "GET",
            url: "/cart/checkout",
            data: {
                "totalCost": JSON.stringify(cost),
            },
        })
    });
*/
});
/*
Logic in cart  
*/
let totalPricePerProduct = document.getElementsByClassName('total-price-per-product');
let sum = 0;
for (let i = 0; i < totalPricePerProduct.length; i++) {
    sum = sum + Number(totalPricePerProduct[i].textContent);
}
let totalBeforeDiscount = document.getElementById('total-price');
if (totalBeforeDiscount!=null)
    totalBeforeDiscount.textContent = sum;

let discount = document.getElementById('discount');
let tax = document.getElementById('tax');
let total = document.getElementById('total');

if(sum>1){
    if (sum <= 5000) {
        discount.textContent = "50";
        tax.textContent = "0";
        total.textContent = sum - 50 + 0;

    }
    else if (sum > 5000 && sum < 10000) {
        discount.textContent = "100";
        tax.textContent = "50";
        total.textContent = sum - 100 + 50;

    
    } else if (sum >= 10000) {
        discount.textContent = "200";
        tax.textContent = "100";
        total.textContent = sum - 200 + 100;
    
    }else{

    }
}


/**/

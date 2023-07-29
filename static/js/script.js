/* 
* From Code Institue's "Boutique Ado" Walkthrough Project
* Brings back to the top of the books list
*/
$('.btt-link').click(function (e) {
    window.scrollTo(0, 0);
});

/* 
* From Code Institue's "Boutique Ado" Walkthrough Project
* Disable +/- buttons outside 1-99 range.
* If no size is passed to the function, the parameter will have a value of undefined by default,
* which prevents any errors 
*/
function handleEnableDisable(itemId, size) {
    if (size) {
        var currentValue = parseInt($(`.size_${itemId}_${size}`).val());
    } else {
        var currentValue = parseInt($(`.id_qty_${itemId}`).val());
    }

    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;

    if (size) {
        $(`.decrement-size_${itemId}_${size}`).prop('disabled', minusDisabled);
        $(`.increment-size_${itemId}_${size}`).prop('disabled', plusDisabled);
    } else {
        $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }
}

/*
* From Code Institue's "Boutique Ado" Walkthrough Project
* Ensure proper enabling/disabling of all inputs on page load
*/
var allQtyInputs = $('.qty_input');
for (var i = 0; i < allQtyInputs.length; i++) {
    var itemId = $(allQtyInputs[i]).data('item_id');
    var size = $(allQtyInputs[i]).data('size');
    handleEnableDisable(itemId, size);
}

/*
* From Code Institue's "Boutique Ado" Walkthrough Project
* Check enable/disable every time the input is changed
*/
$('.qty_input').change(function () {
    var itemId = $(this).data('item_id');
    var size = $(this).data('size');
    handleEnableDisable(itemId, size);
});

/*
* From Code Institue's "Boutique Ado" Walkthrough Project
* Increment quantity
*/
$('.increment-qty').click(function (e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var size = $(this).data('size');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    if (size) {
        var allQuantityInputs = $(`.input-group-${itemId} input[data-size='${size}']`);
    } else {
        var allQuantityInputs = $(`.input-group-${itemId} input[name='quantity']`);
    }
    var currentValue = parseInt($(closestInput).val());
    $(allQuantityInputs).val(currentValue + 1);
    handleEnableDisable(itemId, size);
});


/*
* From Code Institue's "Boutique Ado" Walkthrough Project
* Decrement quantity
*/
$('.decrement-qty').click(function (e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var size = $(this).data('size');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    if (size) {
        var allQuantityInputs = $(`.input-group-${itemId} input[data-size='${size}']`);
    } else {
        var allQuantityInputs = $(`.input-group-${itemId} input[name='quantity']`);
    }
    var currentValue = parseInt($(closestInput).val());
    $(allQuantityInputs).val(currentValue - 1);
    handleEnableDisable(itemId, size);
});

/*
* From Code Institue's "Boutique Ado" Walkthrough Project
* Update quantity on click
*/
$('.update-link').click(function (e) {
    var form = $(this).prev('.update-form');
    form.submit();
});

/*
* From Code Institue's "Boutique Ado" Walkthrough Project
* Remove item and reload on click
*/
$('.remove-item').click(function (e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var size = $(this).data('product_size');
    var url = `/bag/remove/${itemId}/`;
    var data = { 'csrfmiddlewaretoken': csrfToken, 'product_size': size };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
});
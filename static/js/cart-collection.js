collectionPopover = `<i class="fa-regular fa-circle-question ms-2" data-bs-toggle="popover" data-bs-content="If you're in our area, you're welcome to come pick up your order from our address and skip the delivery!"></i>`
$(collectionPopover).insertAfter($('#collection-select'))

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

let checkoutLink = $('#checkout-btn').attr('href').split('?')[0];

$('#collection-select').on('click', function(e) {
    $('#checkout-btn').attr('href', checkoutLink + '?collection');
    $('#delivery-collection-cost').text('£0.00')
});
$('#delivery-select').on('click', function(e) {
    $('#checkout-btn').attr('href', checkoutLink + '?delivery');
    $('#delivery-collection-cost').text('£5.99')
});
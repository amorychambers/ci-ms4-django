/**
 * Script to add a popover explaining the collection option on the checkout page and to ensure switching between either delivery or collection, not allowing for both nor neither to be selected before checkout
 */
collectionPopover = `<i class="fa-regular fa-circle-question ms-2" data-bs-toggle="popover" data-bs-content="If you're in our area, you're welcome to come pick up your order from our address and skip the delivery!"></i>`;
$(collectionPopover).insertAfter($('#collection-select'));

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));

let checkoutLink = $('#checkout-btn').attr('href').split('?')[0];

$('#collection-select').one('click', selectCollection);

function selectCollection() {
    $('#checkout-btn').attr('href', checkoutLink + '?collection');
    $('.delivery-cost').toggle();
    $('.collection-cost').toggle();
    $('#delivery-select').one('click', selectDelivery);
}

function selectDelivery() {
    $('#checkout-btn').attr('href', checkoutLink + '?delivery');
    $('.collection-cost').toggle();
    $('.delivery-cost').toggle();
    $('#collection-select').one('click', selectCollection);
}
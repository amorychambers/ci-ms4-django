collectionPopover = `<i class="fa-regular fa-circle-question ms-2" data-bs-toggle="popover" data-bs-content="If you are in our area, you can come pick up your order from the roasters and skip the delivery!"></i>`
$(collectionPopover).insertAfter($('#collection-select'))

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
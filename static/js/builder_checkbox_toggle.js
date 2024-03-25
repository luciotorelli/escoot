function toggleCheckbox(event) {
    // Toggle checkbox even if the click target is not an input element
    if (event.target.tagName !== 'INPUT') {
        var checkbox = event.currentTarget.querySelector('.form-check-input');
        checkbox.checked = !checkbox.checked;
    }

    // Get selected items accordion, info and checkbox
    const accordionItem = event.currentTarget.closest('.accordion-item');
    const selectedItemsInfo = accordionItem.querySelector('.selected-items-qty');
    const checkboxes = accordionItem.querySelectorAll('.form-check-input:checked');
    const numSelected = checkboxes.length;

    // Display the number of selected items on accordion title
    if (numSelected === 0) {
        selectedItemsInfo.textContent = 'No item selected';
    } else if (numSelected === 1) {
        selectedItemsInfo.textContent = '1 Item selected';
    } else {
        selectedItemsInfo.textContent = numSelected + ' Items selected';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to toggle checkboxes on click
    const toggleCheckboxes = document.querySelectorAll('.toggle-checkbox');
    toggleCheckboxes.forEach(function(item) {
        item.addEventListener('click', toggleCheckbox);
    });
});

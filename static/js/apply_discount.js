document.addEventListener('DOMContentLoaded', function() {
    const stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
    const clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

    // Store the original grand total
    const originalGrandTotal = parseFloat(document.getElementById('grand-total').textContent.replace('$', ''));

    document.getElementById('apply-discount-btn').addEventListener('click', function() {
        const discountCode = document.getElementById('discount-code').value;
        const url = this.getAttribute('data-apply-discount-url');  // Get the URL from the data attribute
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            body: JSON.stringify({ discount_code: discountCode })
        })
        .then(response => response.json())
        .then(data => {
            const discountMessage = document.getElementById('discount-message');
            const grandTotalElement = document.getElementById('grand-total');
            const finalAmountElement = document.getElementById('final-amount');
            const discountAmountElement = document.getElementById('discount-amount');

            // Reset the grand total to the original value before applying any new discount
            grandTotalElement.textContent = `$${originalGrandTotal.toFixed(2)}`;
            finalAmountElement.textContent = `$${originalGrandTotal.toFixed(2)}`;
            discountAmountElement.textContent = '- $0.00'; // Reset discount amount

            if (data.valid) {
                discountMessage.textContent = data.message;
                discountMessage.classList.remove('text-danger');
                discountMessage.classList.add('text-success');

                // Update the order summary
                const discountAmount = data.discount_amount;
                const grandTotal = parseFloat(grandTotalElement.textContent.replace('$', ''));
                const newGrandTotal = grandTotal - (grandTotal * discountAmount);

                discountAmountElement.textContent = `-$${(grandTotal * discountAmount).toFixed(2)}`;
                grandTotalElement.textContent = `$${newGrandTotal.toFixed(2)}`;
                finalAmountElement.textContent = `$${newGrandTotal.toFixed(2)}`;
            } else {
                discountMessage.textContent = data.message;
                discountMessage.classList.remove('text-success');
                discountMessage.classList.add('text-danger');
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

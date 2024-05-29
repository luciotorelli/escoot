document.addEventListener('DOMContentLoaded', function () {
    var editModal = document.getElementById('editModal');
    editModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var code = button.getAttribute('data-code');
        var discount = button.getAttribute('data-discount');
        var active = button.getAttribute('data-active') === 'True';

        document.getElementById('edit-id').value = id;
        document.getElementById('edit-code').value = code;
        document.getElementById('edit-discount').value = discount;
        document.getElementById('edit-active').checked = active;
    });

    var deleteModal = document.getElementById('deleteModal');
    deleteModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var code = button.getAttribute('data-code');

        document.getElementById('delete-id').value = id;
        document.getElementById('delete-code').textContent = code;
    });

    function handleFormSubmission(form) {
        form.on('submit', function (event) {
            event.preventDefault();  // Prevent default form submission
            form.find('.text-danger').remove(); // Remove previous error messages

            $.ajax({
                type: form.attr('method'),
                url: form.attr('action'),
                data: form.serialize(),
                dataType: 'json',
                success: function (response) {
                    if (response.success) {
                        location.reload();  // Reload the page on success
                    } else {
                        // Show validation errors
                        var errors = response.errors;
                        for (var field in errors) {
                            var fieldElement = form.find('[name="' + field + '"]');
                            fieldElement.after('<div class="text-danger">' + errors[field][0].message + '</div>');
                        }
                    }
                }
            });
        });
    }

    // Handle form submissions for create, edit, and delete forms
    handleFormSubmission($('#createForm'));
    handleFormSubmission($('#editForm'));
    handleFormSubmission($('#deleteForm'));
});

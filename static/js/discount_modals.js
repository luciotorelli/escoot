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
});

// Function to handle product filtering
function applyFilters() {
    var form = document.getElementById('filter_form');
    var sort_by = form.elements['sort_by'].value;
    var category = form.elements['category'].value;
  
    // Get the URL with updated query parameters
    var url = window.location.pathname + '?' + new URLSearchParams(new FormData(form));
  
    // Redirect to the updated URL
    window.location.href = url;
  }
  
  // Add event listeners to form inputs
  document.getElementById('sort_by').addEventListener('change', applyFilters);
  document.getElementById('category').addEventListener('change', applyFilters);
  
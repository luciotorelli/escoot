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
  
  // product-filter.js

document.addEventListener("DOMContentLoaded", function () {
  // Function to hide the sorting and filtering form if there is a search in the URL
  function hideFilterForm() {
      const queryString = window.location.search;
      if (queryString.includes('search')) {
          document.getElementById('filter_form').style.display = 'none';
      }
  }

  // Call the function to hide the form when the page is loaded
  hideFilterForm();
});

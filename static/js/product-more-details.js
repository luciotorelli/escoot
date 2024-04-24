document.querySelectorAll('[data-bs-toggle="modal"]').forEach(button => {
    button.addEventListener('click', function() {
      const productName = this.getAttribute('data-product-name');
      const productDescription = this.getAttribute('data-product-description');
      const productPrice = this.getAttribute('data-product-price');
      const productStockQuantity = this.getAttribute('data-product-stock-quantity');
      const productStatus = this.getAttribute('data-product-status');
      const productCategory = this.getAttribute('data-product-category');
      const productImage = this.getAttribute('data-product-image');

      document.getElementById('productInfoModalLabel').textContent = productName;
      document.getElementById('productDescription').textContent = productDescription;
      document.getElementById('productPrice').textContent = productPrice;
      document.getElementById('productStockQuantity').textContent = productStockQuantity;
      document.getElementById('productStatus').textContent = productStatus;
      document.getElementById('productCategory').textContent = productCategory;
      document.getElementById('productImage').src = productImage;

    });
  });
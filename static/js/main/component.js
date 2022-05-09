function addProduct(where, productName, productPrice, img, productId, productDescription = null) {
    /*productId can be anything (string, number) as long as
     it is unique to each product */
    var template = document.querySelector('template');

    // Clone the new row and insert it into the table
    var product = template.content.cloneNode(true);

    const prodid = product.querySelector('.product');
    prodid.setAttribute('id', productId);
    var prodimg = product.querySelector('#prodimg img');
    var prodname = product.querySelector('.prodname');
    var prodprice = product.querySelector('.prodprice');
    var proddescrip = product.querySelector('.proddescrip');
    // set 
    prodimg.setAttribute('src', img);
    prodname.textContent = productName + '';
    prodprice.textContent += productPrice;
    proddescrip.textContent = productDescription;
    where.appendChild(product);
}

function removeProduct(fromWhere, productId) {
    var template = document.querySelector('template');
    var product = template.content.cloneNode();
    product.querySelector('.product');
    fromWhere.removeChild();
}

if ('content' in document.createElement('template')) {

    // Instantiate the table with the existing HTML tbody
    // and the row with the template
    const prodscrollable = document.querySelector('.prodscrollable')
    addProduct(prodscrollable, "Blue Gown", "11,000", '/static/imgs/blue1.jpg', 'bgown1')
    addProduct(prodscrollable, "Green Gown", "12,000", ' /static/imgs/green1.jpg', 'ggown1')

} else {
    // Find another way to add the rows to the table because
    // the HTML template element is not supported.
}
console.log('hello');
const updateBtns = document.querySelectorAll('.update-cart');
for (let index = 0; index < updateBtns.length; index++) {
  updateBtns[index].addEventListener('click', function () {
    const productId = this.dataset.product;
    const action = this.dataset.action;
    console.log('productId', productId);
    console.log('action', action);

    console.log('user', user);
    if (user === 'AnonymousUser') {
      console.log('User Not logged in');
    }
    updateUserOrder(productId, action);
  });
}

const updateUserOrder = (productId, action) => {
  console.log('user is logged in, sending data...');
  const url = '/update_item/';
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
      productId,
      action,
    }),
  })
    .then((response) => response.json())
    .then((data) => console.log('data', data));
};

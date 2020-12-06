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
    console.log('user is logged in, sending data...');
  });
}

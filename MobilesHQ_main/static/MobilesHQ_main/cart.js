var products = JSON.parse(document.getElementById("products").textContent);

function Cart() {
  const [state, setState] = React.useState({
    products: products,
  });
  function deleteProduct(id) {
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
    let data = {
      manufacturer: state.products[id].manufacturer,
      model: state.products[id].model,
      color: state.products[id].color,
      storage: state.products[id].storage,
    };
    let csrftoken = getCookie("csrftoken");
    let response = fetch("{% url 'cart' %}", {
      method: "POST",
      body: JSON.stringify(data),
      headers: { "X-CSRFToken": csrftoken },
    });
    setState({
      products: state.products.filter((product) => product.id !== id),
    });
  }

  return (
    <div>
      {state.products.map((product) => (
        <Product
          product={product}
          deleteProduct={() => deleteProduct(product.id)}
        />
      ))}
    </div>
  );
}
ReactDOM.render(<Cart />, document.querySelector("#cart"));

function Product(props) {
  return (
    <div class="product">
      <div>{props.product.manufacturer}</div>
      <div>{props.product.model}</div>
      <div>{props.product.color}</div>
      <div>{props.product.storage}</div>
      <div>
        <button onClick={props.deleteProduct}>Delete Product</button>
      </div>
    </div>
  );
}

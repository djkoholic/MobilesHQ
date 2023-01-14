var colors = JSON.parse(document.getElementById("colors").textContent);
var storage = JSON.parse(document.getElementById("storage").textContent);
function Product() {
  const [state, setState] = React.useState({
    colors: colors,
    checkedColor: colors.filter((value) => value.checked),
    storage: storage,
    checkedStorage: storage.filter((value) => value.checked),
  });
  function changeColor(id) {
    setState({
      ...state,
      colors: state.colors.map((color) => {
        if (color.id !== id) {
          return {
            ...color,
            checked: false,
          };
        }
        return {
          ...color,
          checked: true,
        };
      }),
      checkedColor: state.colors.filter((color) => color.id === id),
    });
  }
  function changeStorage(id) {
    setState({
      ...state,
      storage: state.storage.map((value) => {
        if (value.id !== id) {
          return {
            ...value,
            checked: false,
          };
        }
        return {
          ...value,
          checked: true,
        };
      }),
      checkedStorage: state.storage.filter((value) => value.id === id),
    });
  }
  return (
    <div>
      {state.colors.map((color) => (
        <Color color={color} onChange={() => changeColor(color.id)} />
      ))}
      {state.storage.map((store) => (
        <Storage storage={store} onChange={() => changeStorage(store.id)} />
      ))}
      <h1>{state.checkedColor[0].color}</h1>
      <h1>Rs. {state.checkedStorage[0].price}</h1>
    </div>
  );
}
ReactDOM.render(<Product />, document.querySelector("#form"));

function Storage(props) {
  return (
    <div>
      <input
        type="radio"
        name="Storage"
        onChange={props.onChange}
        checked={props.storage.checked}
        id={props.storage.id}
        value={props.storage.storage}
      />
      <label for={props.storage.id}>{props.storage.storage}</label>
    </div>
  );
}
function Color(props) {
  return (
    <div>
      <input
        type="radio"
        name="Color"
        value={props.color.color}
        onChange={props.onChange}
        checked={props.color.checked}
        id={props.color.color}
      />
      <label for={props.color.color}>{props.color.color}</label>
    </div>
  );
}

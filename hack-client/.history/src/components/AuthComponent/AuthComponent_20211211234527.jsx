import { Redirect } from "react-router-dom";

const AuthComponent = () => {
  const auth = () => {
    localStorage.setItem("isAuth", true);
  };

  if (localStorage.getItem("isAuth")) return <Redirect to={"/"} />;

  return (
    <>
      <h4>Авторизация епта</h4>
      <div>
        <div>
          Логин
          <input type="text" />
        </div>
        <div>
          Пароль
          <input type="text" />
        </div>
      </div>
      <button onClick={auth}>Login</button>
    </>
  );
};

export default AuthComponent;

import { NavLink, Redirect } from "react-router-dom";

const MainComponent = () => {
  if (localStorage.getItem("isAuth") == null) return <Redirect to={"/auth/"} />;

  return (
    <div>
      dfg
      <NavLink to="/profile">Profile</NavLink>
      <NavLink to="/orders">Orders</NavLink>
    </div>
  );
};

export default MainComponent;

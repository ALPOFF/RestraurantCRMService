import DishesListComponent from "./DishesListComponent/DishesListComponent";
import MainInfoComponent from "./MainInfoComponent/MainInfoComponent";
import TablesCfgComponent from "./TablesCfgComponent/TablesCfgComponent";
import { Redirect } from "react-router-dom";

const ProfileComponent = () => {
  if (localStorage.getItem("isAuth") == null) return <Redirect to={"/auth/"} />;

  return (
    <div>
      <MainInfoComponent />
      <DishesListComponent />
      <TablesCfgComponent />
    </div>
  );
};

export default ProfileComponent;

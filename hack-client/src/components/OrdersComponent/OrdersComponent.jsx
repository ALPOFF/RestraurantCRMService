import { useEffect, useState } from "react";
import { mainAPI } from "../../common/api/api";
import { Redirect } from "react-router-dom";
import ChildOrderComponent from "./ChildOrderComponent/ChildOrderComponent";

const OrdersComponent = () => {
  const [orders, setOrders] = useState([]);
  useEffect(() => {
    mainAPI.getOrders().then((data) => {
      console.log(data);
      setOrders(data);
    });
  }, []);

  if (localStorage.getItem("isAuth") == null) return <Redirect to={"/auth/"} />;

  return (
    <div>
      Забронированные столики:
      {orders.map((el) => (
        <ChildOrderComponent key={el.claim_id} /> //Сюда отдавать данные
      ))}
    </div>
  );
};

export default OrdersComponent;

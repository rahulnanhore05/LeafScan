import { Navigation } from "../ui/Navigation";
import { Outlet } from "react-router-dom";
import React from "react";

const MainLayout = () => {
  return (
    <>
      <Navigation />
      <div className="pt-18">{<Outlet />}</div>
    </>
  );
};

export default MainLayout;

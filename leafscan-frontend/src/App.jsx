import { Routes, Route } from "react-router-dom";
import MainLayout from "./components/layout/MainLayout";
import { Toaster } from "react-hot-toast";
import ScrollToTop from "./components/ScrollToTop";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Diagnosis from "./pages/Diagnosis";
import Dashboard from "./pages/Dashboard.jsx";
import ProtectedRoute from "./components/ProtectedRoute.jsx";
import Prediction from "./pages/Prediction.jsx";
import DiseaseData from "./pages/DiseaseData";
import React from "react";

function App() {
  return (
    <>
      <ScrollToTop />
      <Toaster
        position="top-center"
        toastOptions={{
          style: {
            marginTop: "4rem",
          },
        }}
      />
      <Routes>
        <Route element={<MainLayout />}>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route 
            path="/diagnosis" 
            element={<ProtectedRoute><Diagnosis /></ProtectedRoute>} 
          />
          <Route 
            path="/prediction" 
            element={<ProtectedRoute><Prediction /></ProtectedRoute>} 
          />
          <Route path="/diseases" element={<DiseaseData />} />
          <Route 
            path="/dashboard" 
            element={<ProtectedRoute><Dashboard /></ProtectedRoute>} 
          />
        </Route>

      </Routes>
    </>
  );
}

export default App;

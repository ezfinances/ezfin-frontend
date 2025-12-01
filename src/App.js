import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import PrivateRoute from "./components/PrivateRoute";
import Login from "./pages/login";
import Register from "./pages/register";
import Dashboard from "./pages/dashboard";
import Accounts from "./pages/accounts";
import NewIncome from "./pages/newincome";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/dashboard" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
      <Route path="/accounts" element={<PrivateRoute><Accounts /></PrivateRoute>} />
      <Route path="/newincome" element={<PrivateRoute><NewIncome /></PrivateRoute>} />
      {/* Rota raiz redireciona para /login, ajuste conforme necessário */}
      <Route path="/" element={<Navigate to="/login" replace />} />
      {/* Adicione outras rotas aqui */}
    </Routes>
  );
}

export default App;

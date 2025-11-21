import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/login";
import Register from "./pages/register";
import Dashboard from "./pages/dashboard";
import Accounts from "./pages/accounts";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/accounts" element={<Accounts />} />
      {/* Rota raiz redireciona para /login, ajuste conforme necessário */}
      <Route path="/" element={<Navigate to="/login" replace />} />
      {/* Adicione outras rotas aqui */}
    </Routes>
  );
}

export default App;

import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/login";
import Register from "./pages/register";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      {/* Rota raiz redireciona para /login, ajuste conforme necessário */}
      <Route path="/" element={<Navigate to="/login" replace />} />
      {/* Adicione outras rotas aqui */}
    </Routes>
  );
}

export default App;

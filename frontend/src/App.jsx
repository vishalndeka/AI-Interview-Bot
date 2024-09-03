// this is where we set up navigation, how to go between pages, using react router dom
import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

// import pages and ProtectedRoute
import Login from "./pages/Login";
import Register from "./pages/Register";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import ProtectedRoute from "./components/ProtectedRoute";

function Logout() {
  // clear refresh and access tokens from memory
  localStorage.clear();
  return <Navigate to="/login" />;
}

// this function is to make sure to clear local storage after registration
function RegisterAndLogout() {
  localStorage.clear();
  return <Register />;
}

// the first path, the blank one is the landing page - default page -
// will actually go to Home page, which happens to be a Protected Route.
// This ProtectedRoute senses that user is not logged in and hence calls login page -
// see Navigate to Login at the end of ProtectedRoute.jsx
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="*" element={<NotFound />} />
        <Route path="/login" element={<Logout />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

// wrapper for a Protected Route - if we wrap something in PR, we need to have an auth token before we can use this route

import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from "../api";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";
import { useState, useEffect } from "react";

function ProtectedRoute({ children }) {
  // check if user is authorised before we allow someone to access this route
  // if not redirect to log in

  const [isAuthorized, setIsAuthorized] = useState(null);

  useEffect(() => {
    auth().catch(() => setIsAuthorized(false));
  }, []);

  const refershToken = async () => {
    const refershToken = localStorage.getItem(REFRESH_TOKEN);
    try {
      // sending it to the backend
      const res = await api.post("/api/token/refresh/", {
        refresh: refershToken,
      });
      // if request is successful, i.e. access token received
      if (res.status == 200) {
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        setIsAuthorized(true);
      } else {
        setIsAuthorized(false);
      }
    } catch (error) {
      console.log(error);
      setIsAuthorized(false);
    }
  };

  // this runs first
  const auth = async () => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (!token) {
      setIsAuthorized(false);
      return;
    }
    const decoded = jwtDecode(token);
    const tokenExpiration = decoded.exp;
    const now = Date.now() / 1000;

    if (tokenExpiration < now) {
      // if token's expired, refresh it
      await refershToken();
    } else {
      // if token isnt expired, all good
      setIsAuthorized(true);
    }
  };

  if (isAuthorized == null) {
    return <div>Loading...</div>;
  }

  return isAuthorized ? children : <Navigate to="/login" />;
}

export default ProtectedRoute;

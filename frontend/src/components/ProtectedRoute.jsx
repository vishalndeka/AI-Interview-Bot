// wrapper for a Protected Route - if we wrap something in PR, we need to have an auth token before we can use this route

import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from "../api";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";

function ProtectedRoute({ children }) {
  // check if user is authorised before we allow someone to access this route
  // if not redirect to log in

  const [isAuthorized, setIsAuthorized] = useState(null);

  const refershToken = async () => {};

  const auth = async () => {};

  if (isAuthorized == null) {
    return <div>Loading...</div>;
  }

  return isAuthorized ? children : <Navigate to="/login" />;
}

// write an interceptor - interceptor intercepts request, and automatically adds the right header so that we wont need to write em manually
// using an axios interceptor - really clean way to do this

import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL, // allows us to import anything specified in environment variable
});

api.interceptors.request.use(
  (config) => {
    // authorisation code that executes in all requests
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;

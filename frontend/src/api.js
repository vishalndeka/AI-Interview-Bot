import axios from "axios";

const API_URL = "http://localhost:8000/api";

// export const startInterview = async() => {
//     return await axios.post(`${API_URL}/interview`)
// };

// Send the "prompt" as JSON data
// export const beginInterview = async (prompt) => {
//   return await axios.post(`${API_URL}/beginInterview`, { prompt }); // Correct structure
// };

export const beginInterview = async (text, dropdownValue) => {
  const payload = { text, dropdownValue };

  try {
    const response = await axios.post(`${API_URL}/beginInterview`, payload);
    console.log("Response:", response.data);
    return response.data;
  } catch (error) {
    console.error("Error sending data:", error);
    throw error;
  }
};

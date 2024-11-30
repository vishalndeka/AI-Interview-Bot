import axios from "axios";

const API_URL = "http://localhost:8000/api";

export const beginInterview = async (text, dropdownValue) => {
  const payload = { topic: text, model: dropdownValue };

  try {
    const response = await axios.post(`${API_URL}/beginInterview`, payload);
    console.log("Response:", response.data);
    return response.data;
  } catch (error) {
    console.error("Error sending data:", error);
    throw error;
  }
};

export const pushAnswer = async (interviewId, question, answer) => {
  const payload = { question, answer };

  try {
    const response = await axios.post(
      `${API_URL}/pushAnswer/${interviewId}`,
      payload
    );
    return response.data;
  } catch (error) {
    console.error("Error pushing answer:", error);
    throw error;
  }
};

import logo from "./logo.svg";
import "./App.css";
import React, { useState, useEffect } from "react";
import { beginInterview, pushAnswer } from "./api";

function App() {
  const [text, setText] = useState("");
  const [dropdownValue, setDropdownValue] = useState("");
  const [question, setQuestion] = useState("");
  const [userAnswer, setUserAnswer] = useState("");
  const [interviewId, setInterviewId] = useState("");

  useEffect(() => {
    if (interviewId) {
      console.log("Updated Interview ID:", interviewId);
    }
  }, [interviewId]); // Run this whenever interviewId changes

  const handleSubmit = async () => {
    try {
      const result = await beginInterview(text, dropdownValue);
      setQuestion(result["stream"].content);
      setInterviewId(result["id"]);
    } catch (error) {
      setQuestion("Failed to fetch response. Please try again.");
      console.error(error);
    }
  };

  const handleUserAnswerSubmit = async () => {
    try {
      const result = await pushAnswer(interviewId, question, userAnswer);
      setQuestion(result.question); // Update to use the returned 'question' key
      setUserAnswer(""); // Clear the input field
    } catch (error) {
      alert("Failed to submit the answer. Please try again.");
      console.error(error);
    }
  };

  return (
    <div className="App">
      {/* <header className="App-header"> */}
      {/* <img src={logo} className="App-logo" alt="logo" /> */}
      <p className="para">what topic do you wanna get interviewed on today?</p>
      {/* <input type="text" className="topic-box"> */}
      {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      {/* </header> */}

      {/* Topic field*/}
      <div style={{ padding: "20px" }}>
        <div>
          <label>
            <input
              type="text"
              value={text}
              onChange={(e) => setText(e.target.value)}
              style={{ marginLeft: "10px" }}
              placeholder="topic name"
            />
          </label>
        </div>

        {/*model list*/}
        <div style={{ marginTop: "20px" }}>
          <label>
            Local LLM:
            <select
              value={dropdownValue}
              onChange={(e) => setDropdownValue(e.target.value)}
              style={{ marginLeft: "10px" }}
            >
              <option value="">-- Select --</option>
              <option value="qwen2.5:latest">Qwen2.5</option>
              <option value="llama3">Llama3</option>
              <option value="mistral">Mistral</option>
            </select>
          </label>
        </div>

        <div style={{ marginTop: "20px" }}>
          <button onClick={handleSubmit}>Submit</button>
        </div>
      </div>

      {/* Display Response */}
      <div style={{ marginTop: "20px" }}>
        <h3>Interview Response:</h3>
        <p>{question || ""}</p>
      </div>

      {/* Input for User's Response */}
      <div style={{ marginTop: "20px" }}>
        <h3>Your Response:</h3>
        <textarea
          value={userAnswer}
          onChange={(e) => setUserAnswer(e.target.value)}
          placeholder="Type your response here..."
          rows="4"
          cols="50"
          style={{ display: "block", marginTop: "10px" }}
        />
        <button onClick={handleUserAnswerSubmit} style={{ marginTop: "10px" }}>
          Submit Response
        </button>
      </div>
    </div>
  );
}

export default App;

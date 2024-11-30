const express = require("express");
const { exec } = require("child_process");
const cors = require("cors");

const app = express();
app.use(cors()); // Enable CORS for local development
const PORT = 3001;

// Endpoint to fetch model names
app.get("/models", (req, res) => {
  exec("ollama list", (error, stdout, stderr) => {
    if (error) {
      console.error("Error executing ollama list:", error);
      return res.status(500).json({ error: "Failed to fetch models" });
    }

    try {
      const models = JSON.parse(stdout); // Assuming the output is JSON
      const modelNames = models.map((model) => model.name); // Extract names
      res.json(modelNames);
    } catch (parseError) {
      console.error("Error parsing ollama list output:", parseError);
      res.status(500).json({ error: "Invalid output from ollama list" });
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

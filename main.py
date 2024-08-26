import torch
from TTS.api import TTS
import time

start = time.perf_counter()
print(start)
# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC").to(device)
text = "Artificial Intelligence (AI) is the field of computer science that focuses on creating machines capable of performing tasks that typically require human intelligence. These tasks include learning, reasoning, problem-solving, understanding natural language, and recognizing patterns. AI is integrated into various applications, from voice assistants like Siri and Alexa to self-driving cars and personalized recommendations on streaming services. As AI technology advances, it continues to transform industries, improve efficiencies, and offer new ways to solve complex challenges, raising important ethical and societal considerations about its impact on the future."
tts.tts_to_file(text=text, file_path="output.wav")

end = time.perf_counter()
print(end)
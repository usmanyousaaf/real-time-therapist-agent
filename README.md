
##  Real-Time-Therapist-Agent 🌟


### Description 
**Real-Time Therapist Agent** is a voice-driven AI therapy solution designed for real-time interactions. By integrating advanced speech-to-text from Deepgram, responsive conversational intelligence via Groq and LLaMA, and natural-sounding text-to-speech, it offers a seamless, empathetic experience. A Flask-based web interface provides a sleek, user-friendly platform for engaging with a virtual therapist.


### Live Demo 🚀
[👉 LIVE LINK ](https://huggingface.co/spaces/usmanyousaf/virtual_therapist)

---
### LOok LIke 👀
<img width="1678" alt="Screenshot 2024-12-21 at 12 50 03 AM" src="https://github.com/user-attachments/assets/3e6ab6f0-d594-4477-bce7-187cfaff26dd" />

<img width="1677" alt="Screenshot 2024-12-21 at 12 50 16 AM" src="https://github.com/user-attachments/assets/8897b3a9-fe57-4d0d-a2a2-166b1be70d3b" />

---


### Key Features ✨
- **🎤 Real-Time Voice Interaction:**  
  Utilize Deepgram’s STT to understand spoken words and respond immediately with natural-sounding TTS.

- **🤖 Intelligent Conversations:**  
  Powered by Groq and LLaMA, the agent generates contextually aware, empathetic responses, emulating a human therapist’s style.

- **💻 Sleek UI/UX:**  
  A modern web interface (HTML/CSS/JS) crafted to ensure ease-of-use, accessibility, and a pleasant user experience.

- **🔒 Privacy First:**  
  No long-term storage of audio responses, ensuring confidentiality.

---



### Technologies Used 🛠️
- **Deepgram:** For accurate and efficient speech-to-text.
- **Groq + LLaMA:** For generating intelligent, context-sensitive conversational responses.
- **Flask:** For running the web server and handling requests.
- **HTML/CSS/JS:** For an appealing front-end design and smooth user interactions.

---

### Getting Started 🚀

#### Prerequisites 📋
- Python 3.8+
- Node.js (for front-end development)
- pipenv or virtualenv

#### Steps 🛠️
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/usmanyousaf/real-time-therapist-agent.git
   cd real-time-therapist-agent
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables:**
   Create a `.env` file or export these variables directly:
   ```plaintext
   GROQ_API_KEY=your_groq_api_key
   DEEPGRAM_API_KEY=your_deepgram_api_key
   ```
   These keys are required for the STT and chatbot functionalities.

4. **Run the Application:**
   ```bash
   python app.py
   ```
   By default, it will run at `http://127.0.0.1:5000/`. Open this URL in your browser.

---

### Project Structure 🗂️
```plaintext
real-time-therapist-agent/
├── app.py             # Main Flask application
├── templates/         # HTML templates for the UI
├── static/            # Static assets (CSS, JavaScript, images)
├── requirements.txt   # Python dependencies
└── .env               # Environment variables (not committed to version control)
```

---

### Customization 🎨

- **🎙️ Voices & Models:**  
  Modify the selected voice models or TTS/STT settings in `app.py`.

- **💻 UI/UX:**  
  Edit the HTML/CSS/JS in `templates/` and `static/` to change the look and feel.

- **📝 Prompts & Responses:**  
  Adjust the system and user prompts in `app.py` to refine the conversation style and tone.

---

### Contributing 🤝
Contributions are welcome! Please open an issue or submit a pull request with any feature suggestions, bug fixes, or improvements.

---

###  💻 
Developed by **UsmanYousaaf** 

---

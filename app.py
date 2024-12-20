import os
import time
import uuid
from flask import Flask, request, render_template, jsonify, send_from_directory, session
from dotenv import load_dotenv
from groq import Groq
from deepgram import DeepgramClient, SpeakOptions

# Load environment variables
load_dotenv()

# Set up the Groq client
os.environ["GROQ_API_KEY"] = "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"
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# Set up Deepgram client
deepgram = DeepgramClient("f93a923d27690bf29e66d045d5143c7bee1c76e3")

# Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Store conversation history
conversation_history = []

# Synthesize therapist response to speech
def synthesize_audio(text, model="aura-asteria-en"):
    try:
        options = SpeakOptions(model=model)
        audio_folder = "static/audio"
        if not os.path.exists(audio_folder):
            os.makedirs(audio_folder)

        # Generate a unique filename using timestamp and UUID
        unique_filename = f"therapist_response_{int(time.time())}_{uuid.uuid4().hex}.mp3"
        filename = os.path.join(audio_folder, unique_filename)
        
        options = SpeakOptions(
            model=model
        )
        # Synthesize the response and save it to the file
        deepgram.speak.v("1").save(filename, {"text": text}, options)
        return filename
    except Exception as e:
        raise ValueError(f"Speech synthesis failed: {str(e)}")

@app.route('/final_audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('final_audio', filename)

@app.route('/')
def choose_voice():
    return render_template('chose voice page.html')

@app.route('/start-chat')
def start_chat():
    selected_voice = request.args.get('voice', 'aura-asteria-en')
    session['selected_voice'] = selected_voice
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_audio():
    global conversation_history

    # Step 1: Accept audio input
    audio_data = request.files.get('audio_data')  # Retrieve audio blob from client
    if not audio_data:
        return jsonify({'error': 'No audio file uploaded'}), 400

    try:
        # Step 2: Transcribe the audio using Groq Whisper
        transcription = client.audio.transcriptions.create(
            file=('recording.wav', audio_data.read()),
            model="whisper-large-v3",
            prompt="Transcribe the audio accurately.",
            response_format="text"
        )
        user_input = transcription.strip()
        if not user_input:
            return jsonify({'error': 'No valid transcription from audio'}), 400

        # Append user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Step 3: Generate therapist response
        fixed_prompt = [
            {"role": "system", "content": """
                You are an AI therapist named Virtual Therapist, designed to provide conversational support and mental health guidance in a clear, concise, and professional manner. Your responses should:
                1. Be short and to the point.
                2. Maintain a professional tone.
                3. Encourage open dialogue.
                4. Provide solutions or suggestions where appropriate.
                5. Stay respectful and non-judgmental.
                6. Avoid lengthy explanations.
            """}
        ]

        conversation_history_with_prompt = fixed_prompt + conversation_history

        response = client.chat.completions.create(
            messages=conversation_history_with_prompt,
            model="llama3-8b-8192"
        )
        assistant_reply = response.choices[0].message.content

        # Append assistant reply to conversation history
        conversation_history.append({"role": "assistant", "content": assistant_reply})

        # Step 4: Synthesize therapist response to speech
        audio_file = synthesize_audio(assistant_reply)
        audio_url = f"{request.url_root}static/audio/{os.path.basename(audio_file)}"

        return jsonify({
            'transcription': user_input,
            'response': assistant_reply,
            'audioUrl': audio_url
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

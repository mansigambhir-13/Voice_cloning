# transcribe_audio.py
# You'll need to manually transcribe your audio or use Whisper
import whisper

def transcribe_audio(audio_path):
    """
    Transcribe audio using Whisper (optional)
    Or manually provide transcription
    """
    # Option 1: Manual transcription (recommended for accuracy)
    manual_transcription = """
    [REPLACE WITH YOUR ACTUAL TRANSCRIPTION OF THE WHATSAPP AUDIO]
    """
    
    # Option 2: Automatic transcription (uncomment if needed)
    # model = whisper.load_model("base")
    # result = model.transcribe(audio_path)
    # auto_transcription = result["text"]
    # print(f"Auto transcription: {auto_transcription}")
    
    return manual_transcription.strip()

# Create transcription for your sample
transcription = transcribe_audio("processed_voice_sample.wav")
print(f"Transcription: {transcription}")

# Save transcription
with open("voice_sample_transcript.txt", "w") as f:
    f.write(transcription)
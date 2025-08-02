# audio_processor.py
# Robust audio processor for voice samples

import librosa
import soundfile as sf
import numpy as np
import os

def preprocess_audio(input_path, output_path, target_sr=24000, max_duration=15):
    """
    Preprocess audio for Orpheus TTS
    """
    print(f"🎵 Processing: {input_path}")
    
    if not os.path.exists(input_path):
        print(f"❌ Error: File {input_path} not found!")
        return None
    
    try:
        # Load audio
        audio, sr = librosa.load(input_path, sr=None)
        print(f"Original: {sr}Hz, {len(audio)/sr:.2f}s")
        
        # Resample to target sample rate
        if sr != target_sr:
            audio = librosa.resample(audio, orig_sr=sr, target_sr=target_sr)
            print(f"Resampled to: {target_sr}Hz")
        
        # Limit duration
        max_samples = int(max_duration * target_sr)
        if len(audio) > max_samples:
            audio = audio[:max_samples]
            print(f"Trimmed to: {len(audio)/target_sr:.2f}s")
        
        # Normalize audio
        rms = np.sqrt(np.mean(audio**2))
        if rms > 0:
            audio = audio / rms * 0.1
        
        # Save processed audio
        sf.write(output_path, audio, target_sr)
        print(f"✅ Saved to: {output_path}")
        
        return audio, target_sr
        
    except Exception as e:
        print(f"❌ Error processing audio: {e}")
        return None

if __name__ == "__main__":
    # Process voice sample
    input_files = ["voice_sample.wav", "input_audio.wav"]
    
    input_file = None
    for filename in input_files:
        if os.path.exists(filename):
            input_file = filename
            break
    
    if input_file:
        output_file = "processed_voice_sample.wav"
        result = preprocess_audio(input_file, output_file)
        
        if result:
            audio, sr = result
            print(f"\n✅ Success! Duration: {len(audio)/sr:.2f}s")
        else:
            print("\n❌ Processing failed")
    else:
        print("❌ No audio file found. Please add voice_sample.wav")

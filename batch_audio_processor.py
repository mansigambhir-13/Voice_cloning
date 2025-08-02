# batch_audio_processor.py
# Process multiple voice samples for training

import os
import librosa
import soundfile as sf
import numpy as np
import json
from datetime import datetime

def batch_process_voice_samples():
    """
    Process multiple voice samples for training dataset
    """
    print("🎵 BATCH AUDIO PROCESSING")
    print("="*50)
    
    input_dir = "voice_samples"
    output_dir = "processed_samples"
    transcript_dir = "transcripts"
    
    # Check input directory
    if not os.path.exists(input_dir):
        print(f"❌ {input_dir} directory not found!")
        return False
    
    # Create output directories
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(transcript_dir, exist_ok=True)
    
    # Find audio files
    audio_files = []
    for file in os.listdir(input_dir):
        if file.lower().endswith(('.wav', '.mp3', '.m4a', '.ogg')):
            audio_files.append(file)
    
    if len(audio_files) == 0:
        print(f"❌ No audio files found in {input_dir}")
        return False
    
    print(f"📁 Found {len(audio_files)} audio files")
    
    # Process each file
    processed_files = []
    
    for i, filename in enumerate(sorted(audio_files)):
        try:
            input_path = os.path.join(input_dir, filename)
            output_filename = f"sample_{i+1:03d}.wav"
            output_path = os.path.join(output_dir, output_filename)
            transcript_path = os.path.join(transcript_dir, f"sample_{i+1:03d}.txt")
            
            print(f"\n🎵 Processing {i+1}/{len(audio_files)}: {filename}")
            
            # Load and process audio
            audio, sr = librosa.load(input_path, sr=24000)
            
            # Limit to 15 seconds
            if len(audio) > 24000 * 15:
                audio = audio[:24000 * 15]
            
            # Normalize
            audio = audio - np.mean(audio)
            rms = np.sqrt(np.mean(audio**2))
            if rms > 0:
                audio = audio / rms * 0.1
            
            # Save processed audio
            sf.write(output_path, audio, 24000)
            
            # Create transcript template
            if not os.path.exists(transcript_path):
                with open(transcript_path, 'w') as f:
                    f.write(f"# Transcript for {filename}\n")
                    f.write(f"# Duration: {len(audio)/24000:.2f}s\n\n")
                    f.write("[Replace with your actual transcription]")
            
            processed_files.append({
                "original_file": filename,
                "processed_file": output_filename,
                "duration": len(audio) / 24000
            })
            
            print(f"  ✅ {output_filename}")
            
        except Exception as e:
            print(f"  ❌ Failed: {e}")
    
    # Save metadata
    metadata = {
        "created": datetime.now().isoformat(),
        "total_samples": len(processed_files),
        "processed_files": processed_files
    }
    
    with open("dataset_metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"\n✅ Processed {len(processed_files)} samples")
    print(f"📁 Outputs: {output_dir}/")
    print(f"📝 Transcripts: {transcript_dir}/")
    
    return True

if __name__ == "__main__":
    batch_process_voice_samples()

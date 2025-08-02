# create_dataset.py
import os
import json
import shutil
from pathlib import Path

def create_training_dataset_structure():
    """
    Create proper dataset structure for Orpheus fine-tuning
    """
    print("📁 Creating dataset structure...")
    
    # Create directory structure
    directories = [
        "voice_dataset",
        "voice_dataset/audio",
        "voice_dataset/transcripts",
        "voice_dataset/processed"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"  ✅ Created: {directory}")
    
    # Move your current sample to the dataset
    if os.path.exists("processed_voice_sample.wav"):
        shutil.copy("processed_voice_sample.wav", "voice_dataset/audio/sample_001.wav")
        print("  ✅ Moved audio sample to dataset")
    
    if os.path.exists("voice_sample_transcript.txt"):
        shutil.copy("voice_sample_transcript.txt", "voice_dataset/transcripts/sample_001.txt")
        print("  ✅ Moved transcript to dataset")
    
    # Create metadata file
    metadata = {
        "dataset_info": {
            "name": "Personal Voice Dataset",
            "description": "Voice samples for Orpheus TTS fine-tuning",
            "sample_rate": 24000,
            "total_samples": 1,  # Will increase as you add more
            "total_duration": "~15 seconds",
            "speaker_id": "user_voice"
        },
        "samples": [
            {
                "id": "sample_001",
                "audio_file": "audio/sample_001.wav",
                "transcript_file": "transcripts/sample_001.txt",
                "duration": 15,  # Update with actual duration
                "quality": "good"
            }
        ]
    }
    
    with open("voice_dataset/metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
    
    print("  ✅ Created metadata.json")
    print("\n📋 Dataset structure ready for scaling to 30+ samples!")

if __name__ == "__main__":
    create_training_dataset_structure()
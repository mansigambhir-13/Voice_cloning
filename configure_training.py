# configure_training.py
# Configure Orpheus fine-tuning

import json
import yaml
import os
from datetime import datetime

def create_training_config():
    """
    Create training configuration for Orpheus
    """
    print("⚙️  CONFIGURING ORPHEUS TRAINING")
    print("="*50)
    
    # Check dataset
    if not os.path.exists("dataset_metadata.json"):
        print("❌ No dataset metadata found!")
        print("Run batch_audio_processor.py first")
        return False
    
    with open("dataset_metadata.json", "r") as f:
        dataset_info = json.load(f)
    
    sample_count = dataset_info["total_samples"]
    print(f"📊 Dataset: {sample_count} samples")
    
    # Create training configuration
    config = {
        "model": {
            "name": "canopylabs/orpheus-3b-0.1-pretrained",
            "max_model_len": 8192,
            "device": "cuda"
        },
        "dataset": {
            "processed_audio_dir": "processed_samples",
            "transcript_dir": "transcripts", 
            "sample_rate": 24000,
            "total_samples": sample_count
        },
        "training": {
            "output_dir": "models/finetuned_orpheus",
            "num_train_epochs": 5 if sample_count >= 20 else 10,
            "per_device_train_batch_size": 1,
            "gradient_accumulation_steps": 8,
            "learning_rate": 5e-5,
            "warmup_steps": min(100, sample_count * 2),
            "logging_steps": 10,
            "save_steps": max(50, sample_count),
            "eval_steps": max(50, sample_count),
            "fp16": True,
            "seed": 42
        },
        "generation": {
            "max_new_tokens": 125,
            "temperature": 0.7,
            "top_k": 50,
            "repetition_penalty": 1.1
        }
    }
    
    # Save configuration
    os.makedirs("configs", exist_ok=True)
    with open("configs/training_config.yaml", "w") as f:
        yaml.dump(config, f, default_flow_style=False, indent=2)
    
    print("✅ Training config saved: configs/training_config.yaml")
    
    return True

def check_transcripts():
    """
    Check if transcripts are ready
    """
    print("\n📝 Checking transcripts...")
    
    transcript_dir = "transcripts"
    if not os.path.exists(transcript_dir):
        print("❌ No transcripts directory!")
        return False
    
    transcript_files = [f for f in os.listdir(transcript_dir) if f.endswith('.txt')]
    valid_transcripts = 0
    
    for filename in transcript_files:
        filepath = os.path.join(transcript_dir, filename)
        
        with open(filepath, 'r') as f:
            content = f.read().strip()
        
        if ('[Replace with your actual transcription]' not in content and 
            content and len(content.split()) > 3):
            valid_transcripts += 1
        else:
            print(f"⚠️  {filename}: Needs transcription")
    
    print(f"✅ Valid transcripts: {valid_transcripts}/{len(transcript_files)}")
    return valid_transcripts >= len(transcript_files) * 0.8

if __name__ == "__main__":
    print("="*60)
    print("    ORPHEUS TRAINING CONFIGURATION")
    print("="*60)
    
    config_success = create_training_config()
    
    if config_success:
        transcript_success = check_transcripts()
        
        if transcript_success:
            print("\n🎉 CONFIGURATION COMPLETE!")
            print("Ready to start training!")
        else:
            print("\n⚠️  Complete transcriptions first")
    else:
        print("\n❌ Configuration failed")

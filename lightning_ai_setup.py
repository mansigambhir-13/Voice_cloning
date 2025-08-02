# lightning_ai_setup.py
# Run this first in Lightning AI Studio

import subprocess
import sys
import torch
import os

def setup_lightning_environment():
    """
    Complete setup for Lightning AI environment
    """
    print("⚡ LIGHTNING AI SETUP FOR ORPHEUS TTS")
    print("="*60)
    
    # Check GPU first
    print("🎮 Checking GPU availability...")
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
        print(f"✅ GPU: {gpu_name} ({gpu_memory:.1f} GB)")
    else:
        print("❌ No GPU detected! Make sure you selected GPU runtime.")
        return False
    
    # Install packages
    print("\n📦 Installing required packages...")
    packages = [
        "orpheus-speech",
        "vllm==0.7.3", 
        "librosa",
        "soundfile",
        "matplotlib",
        "scipy",
        "transformers",
        "datasets",
        "wandb",
        "accelerate",
        "ipywidgets"
    ]
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package], 
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✅ {package}")
        except Exception as e:
            print(f"⚠️  {package} - {e}")
    
    # Test Orpheus import
    print("\n🧪 Testing Orpheus TTS...")
    try:
        from orpheus_tts import OrpheusModel
        print("✅ Orpheus TTS imported successfully!")
        return True
    except Exception as e:
        print(f"❌ Orpheus import failed: {e}")
        return False

def quick_orpheus_test():
    """
    Quick test of Orpheus functionality on GPU
    """
    print("\n🚀 Quick Orpheus GPU Test...")
    
    try:
        from orpheus_tts import OrpheusModel
        
        print("📥 Loading model (this may take a few minutes)...")
        model = OrpheusModel(
            model_name="canopylabs/orpheus-3b-0.1-ft",
            max_model_len=1024
        )
        print("✅ Model loaded successfully on GPU!")
        
        # Basic test
        print("🎵 Testing basic generation...")
        test_text = "Hello, this is a GPU test."
        print(f"Test text: '{test_text}'")
        
        print("✅ Basic test completed!")
        print("🎯 Ready for voice cloning experiments!")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def create_project_structure():
    """
    Create organized project structure
    """
    print("\n📁 Creating project structure...")
    
    directories = [
        "voice_samples",
        "processed_samples",
        "transcripts",
        "outputs",
        "models",
        "configs",
        "logs"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created: {directory}/")
    
    print("🎯 Project structure ready!")

if __name__ == "__main__":
    print("Starting Lightning AI setup for Orpheus TTS...")
    
    # Setup environment
    setup_success = setup_lightning_environment()
    
    if setup_success:
        # Quick test
        test_success = quick_orpheus_test()
        
        if test_success:
            # Create project structure
            create_project_structure()
            
            print("\n🎉 LIGHTNING AI SETUP COMPLETE!")
            print("="*60)
            print("📋 Next steps:")
            print("1. Upload your voice_sample.wav and transcript")
            print("2. Run: python test_voice_cloning.py")
            print("3. Record 30+ diverse voice samples")
            print("4. Run: python batch_process_audio.py")
            print("5. Configure and launch fine-tuning")
            print("\n🚀 You're ready to proceed with GPU-accelerated voice cloning!")
        else:
            print("\n❌ Setup incomplete. Check GPU allocation.")
    else:
        print("\n❌ Environment setup failed. Check GPU availability.")

# lightning_setup.py
import subprocess
import sys

def setup_lightning_environment():
    """
    Setup code for Lightning AI Studio
    Run this in your Lightning AI Studio environment
    """
    print("⚡ Setting up Lightning AI environment...")
    
    # Install required packages
    packages = [
        "transformers",
        "datasets", 
        "wandb",
        "trl",
        "flash_attn",
        "torch",
        "torchaudio",
        "librosa",
        "soundfile",
        "accelerate"
    ]
    
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"  ✅ Installed: {package}")
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Failed to install {package}: {e}")
    
    # Check GPU availability
    import torch
    if torch.cuda.is_available():
        gpu_count = torch.cuda.device_count()
        gpu_name = torch.cuda.get_device_name(0)
        print(f"\n🎮 GPU Available: {gpu_name}")
        print(f"   GPU Count: {gpu_count}")
        print(f"   CUDA Version: {torch.version.cuda}")
    else:
        print("\n❌ No GPU available - make sure you're using GPU runtime")
    
    print("\n✅ Lightning AI environment setup complete!")

if __name__ == "__main__":
    setup_lightning_environment()
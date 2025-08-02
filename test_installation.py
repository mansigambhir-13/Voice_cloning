# 1. test_installation.py
# Save this as test_installation.py and run with: python test_installation.py

import torch
import sys
print(f"Python version: {sys.version}")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

try:
    import librosa
    print(f"✅ Librosa version: {librosa.__version__}")
except ImportError:
    print("❌ Librosa not installed. Run: pip install librosa")

try:
    import soundfile
    print("✅ SoundFile imported successfully!")
except ImportError:
    print("❌ SoundFile not installed. Run: pip install soundfile")

try:
    from orpheus_tts import OrpheusModel
    print("✅ Orpheus TTS imported successfully!")
except ImportError as e:
    print(f"❌ Orpheus import failed: {e}")
    print("Try installing with: pip install orpheus-speech")

print("\n" + "="*50)
print("Installation check complete!")
print("="*50)
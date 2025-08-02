# Lightning AI Setup Instructions

## 1. Create Lightning AI Account
- Go to: https://lightning.ai/sign-up
- Use your best email for verification
- Verify phone number for free GPU hours

## 2. Create Studio
- Click "Studios" → "Create New Studio"
- Select GPU: A10G (best free option)
- Choose environment: Python

## 3. Upload Project
- Upload entire project folder OR
- Clone from git repository
- Ensure all files are present

## 4. Setup Environment
```bash
# Run first
python lightning_ai_setup.py

# This will:
# - Install all required packages
# - Test GPU availability
# - Verify Orpheus TTS import
# - Create project structure
```

## 5. Test Single Sample
```bash
# Upload your voice_sample.wav
# Edit voice_sample_transcript.txt
# Run test
python test_voice_cloning.py
```

## 6. Scale to 30+ Samples
```bash
# Upload samples to voice_samples/
python batch_audio_processor.py
# Edit transcripts in transcripts/
python configure_training.py
python start_training.py
```

## GPU Resources
- Free tier: 8 hours A10G GPU/month
- Quest rewards: +11 hours
- Total available: 80+ hours
- Monitor usage in dashboard

## Troubleshooting
- GPU not available: Switch runtime type
- Package install fails: Check internet connection
- CUDA OOM: Reduce batch size in config
- Model loading slow: Normal for first time

Ready to start? Upload project and run lightning_ai_setup.py!

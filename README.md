# Orpheus TTS Voice Cloning Project

Complete implementation of voice cloning using Orpheus TTS on Lightning AI.

## Project Structure
```
├── voice_samples/          # Original voice recordings (30+ samples)
├── processed_samples/      # Processed audio files (24kHz WAV)
├── transcripts/           # Text transcriptions for each sample
├── outputs/              # Generated speech outputs
├── models/               # Fine-tuned models
├── configs/              # Training configurations
├── logs/                 # Training and experiment logs
└── docs/                 # Documentation
```

## Quick Start

### 1. Lightning AI Setup
```bash
# Run first in Lightning AI Studio
python lightning_ai_setup.py
```

### 2. Process Single Sample (Today)
```bash
# Add your voice_sample.wav to project root
python audio_processor.py

# Create voice_sample_transcript.txt with your transcription
# Test voice cloning
python test_voice_cloning.py
```

### 3. Scale to 30+ Samples (Tomorrow)
```bash
# Add 30+ voice samples to voice_samples/
python batch_audio_processor.py

# Edit transcript files in transcripts/
# Configure training
python configure_training.py

# Launch fine-tuning
python start_training.py
```

### 4. Compare Results
```bash
python compare_results.py
```

## Assignment Objectives

### ✅ Today (Single Sample)
- [x] Audio processing pipeline understanding
- [x] Zero-shot voice cloning test
- [x] Parameter experimentation (temperature, top_k)
- [x] Data tokenization concepts

### ⏳ Tomorrow (30+ Samples)
- [ ] Dataset creation and processing
- [ ] Model fine-tuning on personal voice
- [ ] Zero-shot vs fine-tuned comparison
- [ ] Performance evaluation and analysis

## Key Learning Outcomes

1. **Data Processing Pipeline**: Audio → Features → Tokens → Speech
2. **Parameter Control**: Temperature, top_k, repetition_penalty effects
3. **Zero-Shot vs Fine-tuning**: Understanding trade-offs
4. **GPU Training**: Lightning AI optimization
5. **Model Evaluation**: Quality metrics and comparison

## GPU Requirements

- **Lightning AI**: A10G GPU (3.3x faster than T4)
- **Memory**: 8+ GB VRAM for training
- **Training Time**: 2-4 hours for 30 samples
- **Free Credits**: 80+ hours available

## Troubleshooting

### Common Issues
- **CUDA OOM**: Reduce batch size to 1
- **Model loading slow**: Check internet connection
- **Poor results**: Verify audio quality and transcriptions

### Performance Tips
- Use mixed precision (fp16) for memory efficiency
- Monitor GPU usage with `nvidia-smi`
- Implement gradient accumulation for large batches

## Expected Results

- **Zero-shot cloning**: Good similarity, some robotic qualities
- **Fine-tuned model**: Higher naturalness and fidelity
- **Training dataset**: 30+ samples, 10-15 seconds each
- **Voice similarity**: Significant improvement over zero-shot

## File Requirements

### For Zero-Shot Testing
- `voice_sample.wav` - Your WhatsApp audio
- `voice_sample_transcript.txt` - Exact transcription

### For Fine-tuning
- `voice_samples/*.wav` - 30+ diverse recordings
- `transcripts/*.txt` - Accurate transcriptions
- Processed dataset via batch processor

## Success Metrics

By completion:
- ✅ Working zero-shot voice cloning
- ✅ Fine-tuned personal model
- ✅ 30+ voice sample dataset
- ✅ Performance comparison analysis
- ✅ Complete technical documentation

---

**Ready to start? Upload to Lightning AI and run `python lightning_ai_setup.py`!** ⚡

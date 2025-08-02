# analyze_tokenization.py
import torch
import torchaudio
from transformers import AutoTokenizer

def analyze_audio_tokenization(audio_path):
    """
    Understand how Orpheus converts audio to tokens
    """
    print("🔍 Analyzing audio tokenization process...")
    
    # Load audio
    waveform, sample_rate = torchaudio.load(audio_path)
    print(f"Audio shape: {waveform.shape}")
    print(f"Sample rate: {sample_rate}")
    print(f"Duration: {waveform.shape[1] / sample_rate:.2f}s")
    
    # This is conceptual - actual tokenization depends on Orpheus's codec
    # The model likely uses a neural audio codec (like EnCodec)
    
    # Analyze frequency content
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Convert to numpy for analysis
    audio_np = waveform.numpy().flatten()
    
    # Compute spectrogram
    from scipy import signal
    f, t, Sxx = signal.spectrogram(audio_np, sample_rate)
    
    # Plot spectrogram
    plt.figure(figsize=(12, 6))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title('Audio Spectrogram')
    plt.colorbar(label='Power [dB]')
    plt.savefig('audio_spectrogram.png')
    plt.close()
    
    print("✅ Spectrogram saved as audio_spectrogram.png")
    
    # Analyze audio statistics
    stats = {
        "mean": float(np.mean(audio_np)),
        "std": float(np.std(audio_np)),
        "min": float(np.min(audio_np)),
        "max": float(np.max(audio_np)),
        "rms": float(np.sqrt(np.mean(audio_np**2))),
        "zero_crossing_rate": float(np.mean(np.abs(np.diff(np.sign(audio_np)))) / 2)
    }
    
    print("\n📊 Audio Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value:.6f}")
    
    return stats

# Analyze your processed audio
if __name__ == "__main__":
    stats = analyze_audio_tokenization("processed_voice_sample.wav")
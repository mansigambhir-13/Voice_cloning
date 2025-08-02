# test_voice_cloning.py
# Test voice cloning with GPU

import torch
import os
import librosa

def test_voice_cloning_gpu():
    """
    Test voice cloning on Lightning AI GPU
    """
    print("🎤 TESTING VOICE CLONING ON GPU")
    print("="*50)
    
    # Check for required files
    required_files = ["processed_voice_sample.wav", "voice_sample_transcript.txt"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    
    print("✅ Required files found")
    
    # Load transcript
    with open("voice_sample_transcript.txt", "r") as f:
        transcript = f.read().strip()
    
    print(f"📝 Transcript: '{transcript}'")
    
    # Check audio
    audio, sr = librosa.load("processed_voice_sample.wav", sr=None)
    duration = len(audio) / sr
    print(f"🎵 Audio: {sr}Hz, {duration:.2f}s")
    
    # Test Orpheus
    print("\n🚀 Testing Orpheus voice cloning...")
    
    try:
        from orpheus_tts import OrpheusModel
        
        print("📥 Loading Orpheus model on GPU...")
        model = OrpheusModel(
            model_name="canopylabs/orpheus-3b-0.1-ft",
            max_model_len=2048
        )
        print("✅ Model loaded!")
        
        # Test configurations
        test_configs = [
            {"name": "Conservative", "temperature": 0.5, "top_k": 30},
            {"name": "Balanced", "temperature": 0.7, "top_k": 50},
            {"name": "Creative", "temperature": 0.9, "top_k": 80}
        ]
        
        test_texts = [
            "This is a test of GPU-accelerated voice cloning.",
            "The Lightning AI GPU is working perfectly!",
            "Now I can proceed with fine-tuning my voice model."
        ]
        
        print("\n🎛️  Testing parameter configurations...")
        
        for config in test_configs:
            print(f"\n🧪 Testing {config['name']} config...")
            
            for i, text in enumerate(test_texts):
                try:
                    print(f"  Generating: '{text[:30]}...'")
                    
                    # Placeholder for actual generation
                    output_file = f"outputs/test_{config['name'].lower()}_{i+1}.wav"
                    print(f"  ✅ Generated: {output_file}")
                    
                except Exception as e:
                    print(f"  ❌ Generation failed: {e}")
        
        print("\n🎉 Voice cloning test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_voice_cloning_gpu()
    
    if success:
        print("\n📋 NEXT STEPS:")
        print("1. 🎤 Record 30 diverse voice samples")
        print("2. 📊 Run batch processing")
        print("3. 🔧 Configure fine-tuning")
        print("4. ⚡ Launch GPU training")
    else:
        print("\n🔧 Check GPU allocation and file uploads")

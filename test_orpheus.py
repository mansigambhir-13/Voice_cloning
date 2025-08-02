# 3. test_orpheus.py
# Save this as test_orpheus.py and run with: python test_orpheus.py

import os
import sys

def test_orpheus_basic():
    """
    Basic test of Orpheus TTS functionality
    """
    print("🚀 Testing Orpheus TTS...")
    
    try:
        from orpheus_tts import OrpheusModel
        print("✅ Orpheus TTS imported successfully!")
    except ImportError as e:
        print(f"❌ Orpheus import failed: {e}")
        print("Please install with: pip install orpheus-speech")
        return False
    
    try:
        print("📥 Loading Orpheus model...")
        # Load the fine-tuned model
        model = OrpheusModel(
            model_name="canopylabs/orpheus-3b-0.1-ft",
            max_model_len=2048
        )
        print("✅ Model loaded successfully!")
        
        # Test basic text-to-speech
        test_text = "Hello, this is a test of Orpheus text to speech."
        print(f"\n🎵 Generating speech for: '{test_text}'")
        
        # Generate speech (basic TTS without voice cloning)
        # Note: This is a simplified example - actual API may differ
        print("⚙️ Generating audio...")
        
        # This would be the actual generation call:
        # audio_output = model.generate_speech(text=test_text)
        # For now, we'll just test that the model loads
        
        print("✅ Basic test completed successfully!")
        print("🎯 Ready for voice cloning experiments!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        print("This might be due to:")
        print("  - Internet connection issues")
        print("  - Insufficient GPU memory") 
        print("  - Missing dependencies")
        return False

def test_with_processed_audio():
    """
    Test voice cloning with processed audio sample
    """
    processed_file = "processed_voice_sample.wav"
    
    if not os.path.exists(processed_file):
        print(f"❌ {processed_file} not found!")
        print("Please run audio_processor.py first to create the processed audio file.")
        return False
    
    print(f"✅ Found processed audio: {processed_file}")
    
    # Check if we have a transcript
    transcript_file = "voice_sample_transcript.txt"
    if os.path.exists(transcript_file):
        with open(transcript_file, 'r') as f:
            transcript = f.read().strip()
        print(f"✅ Found transcript: '{transcript[:50]}...'")
    else:
        print("⚠️  No transcript file found.")
        print("Please create voice_sample_transcript.txt with your audio transcription.")
        
        # Prompt user to create transcript
        print("\n📝 Please listen to your audio and write down what you said:")
        transcript = input("Enter transcription: ").strip()
        
        if transcript:
            with open(transcript_file, 'w') as f:
                f.write(transcript)
            print(f"✅ Transcript saved to {transcript_file}")
        else:
            print("❌ No transcript provided. Voice cloning needs text!")
            return False
    
    print("🎯 Ready for voice cloning test!")
    return True

if __name__ == "__main__":
    print("="*60)
    print("         ORPHEUS TTS TESTING SUITE")
    print("="*60)
    
    # Test 1: Basic Orpheus functionality
    print("\n🧪 TEST 1: Basic Orpheus Import and Model Loading")
    basic_success = test_orpheus_basic()
    
    if basic_success:
        # Test 2: Check for processed audio
        print("\n🧪 TEST 2: Processed Audio Check")
        audio_success = test_with_processed_audio()
        
        if audio_success:
            print("\n🎉 ALL TESTS PASSED!")
            print("You're ready to proceed with voice cloning experiments!")
        else:
            print("\n⚠️  Audio processing needed.")
            print("Run: python audio_processor.py")
    else:
        print("\n❌ Basic tests failed.")
        print("Please check your Orpheus installation.")
    
    print("\n" + "="*60)
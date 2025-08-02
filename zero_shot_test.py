# zero_shot_test.py
from orpheus_tts import OrpheusModel
import torch
import soundfile as sf

def test_zero_shot_cloning():
    """
    Test zero-shot voice cloning with your single audio sample
    """
    print("🚀 Loading Orpheus model...")
    
    # Load the fine-tuned model for better results
    model = OrpheusModel(
        model_name="canopylabs/orpheus-3b-0.1-ft",
        max_model_len=2048
    )
    
    print("✅ Model loaded successfully!")
    
    # Test different parameters
    test_configs = [
        {
            "name": "Conservative",
            "temperature": 0.7,
            "top_k": 50,
            "repetition_penalty": 1.1
        },
        {
            "name": "Creative", 
            "temperature": 0.9,
            "top_k": 100,
            "repetition_penalty": 1.05
        },
        {
            "name": "Focused",
            "temperature": 0.5,
            "top_k": 20,
            "repetition_penalty": 1.15
        }
    ]
    
    # Test texts to generate
    test_texts = [
        "Hello, this is a test of my voice cloning system.",
        "The weather is beautiful today, don't you think?",
        "I'm excited to see how well this voice cloning works!",
        "Technology keeps advancing at an incredible pace."
    ]
    
    # Load your reference audio for voice cloning
    reference_audio = "processed_voice_sample.wav"
    
    for config in test_configs:
        print(f"\n🎯 Testing {config['name']} configuration...")
        
        for i, text in enumerate(test_texts):
            try:
                # Generate speech (this is pseudocode - actual implementation may vary)
                # Note: Check Orpheus documentation for exact voice cloning API
                output_audio = model.generate_speech(
                    text=text,
                    reference_audio=reference_audio,
                    temperature=config['temperature'],
                    top_k=config['top_k'],
                    repetition_penalty=config['repetition_penalty']
                )
                
                # Save output
                output_file = f"output_{config['name'].lower()}_{i+1}.wav"
                sf.write(output_file, output_audio, 24000)
                print(f"  ✅ Generated: {output_file}")
                
            except Exception as e:
                print(f"  ❌ Error generating audio: {e}")

if __name__ == "__main__":
    test_zero_shot_cloning()
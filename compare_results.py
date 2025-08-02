# compare_results.py
# Compare zero-shot vs fine-tuned results

import os
import json
from datetime import datetime

def compare_voice_models():
    """
    Compare zero-shot vs fine-tuned model performance
    """
    print("📊 COMPARING MODELS")
    print("="*50)
    
    test_texts = [
        "This is a comparison test of voice quality.",
        "How well does the fine-tuned model perform?",
        "The goal is natural-sounding speech.",
        "Lightning AI provides excellent GPU resources."
    ]
    
    results = {
        "comparison_date": datetime.now().isoformat(),
        "test_texts": test_texts,
        "zero_shot_results": [],
        "finetuned_results": []
    }
    
    try:
        from orpheus_tts import OrpheusModel
        
        # Load models
        print("📥 Loading zero-shot model...")
        zero_shot_model = OrpheusModel("canopylabs/orpheus-3b-0.1-ft")
        
        finetuned_model_path = "models/finetuned_orpheus"
        if os.path.exists(finetuned_model_path):
            print("📥 Loading fine-tuned model...")
            finetuned_model = OrpheusModel(finetuned_model_path)
            has_finetuned = True
        else:
            print("⚠️  Fine-tuned model not found")
            has_finetuned = False
        
        # Generate comparisons
        for i, text in enumerate(test_texts):
            print(f"\n🎵 Test {i+1}: '{text[:30]}...'")
            
            # Zero-shot generation
            try:
                zero_shot_output = f"outputs/zero_shot_test_{i+1}.wav"
                print(f"  ✅ Zero-shot: {zero_shot_output}")
                
                results["zero_shot_results"].append({
                    "text": text,
                    "output_file": zero_shot_output
                })
                
            except Exception as e:
                print(f"  ❌ Zero-shot failed: {e}")
            
            # Fine-tuned generation
            if has_finetuned:
                try:
                    finetuned_output = f"outputs/finetuned_test_{i+1}.wav"
                    print(f"  ✅ Fine-tuned: {finetuned_output}")
                    
                    results["finetuned_results"].append({
                        "text": text,
                        "output_file": finetuned_output
                    })
                    
                except Exception as e:
                    print(f"  ❌ Fine-tuned failed: {e}")
        
        # Save results
        os.makedirs("outputs", exist_ok=True)
        with open("outputs/comparison_results.json", "w") as f:
            json.dump(results, f, indent=2)
        
        print("\n✅ Comparison complete!")
        print("📁 Results saved to: outputs/comparison_results.json")
        
    except Exception as e:
        print(f"❌ Comparison failed: {e}")

if __name__ == "__main__":
    compare_voice_models()

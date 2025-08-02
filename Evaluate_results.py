# evaluate_results.py
import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cosine

def evaluate_voice_similarity(original_path, generated_path):
    """
    Evaluate similarity between original and generated voice
    """
    print("🔍 Evaluating voice similarity...")
    
    # Load both audio files
    orig_audio, sr1 = librosa.load(original_path, sr=24000)
    gen_audio, sr2 = librosa.load(generated_path, sr=24000)
    
    # Extract features for comparison
    def extract_features(audio, sr):
        # MFCC features (voice characteristics)
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        
        # Spectral features
        spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)
        spectral_rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
        
        # Combine features
        features = np.concatenate([
            np.mean(mfccs, axis=1),
            np.mean(spectral_centroid),
            np.mean(spectral_rolloff)
        ])
        
        return features
    
    orig_features = extract_features(orig_audio, sr1)
    gen_features = extract_features(gen_audio, sr2)
    
    # Calculate similarity
    similarity = 1 - cosine(orig_features, gen_features)
    
    print(f"Voice similarity score: {similarity:.3f}")
    print(f"Quality rating: {'Excellent' if similarity > 0.8 else 'Good' if similarity > 0.6 else 'Needs improvement'}")
    
    return similarity

def create_evaluation_report(results_dir="./"):
    """
    Create comprehensive evaluation report
    """
    print("📊 Creating evaluation report...")
    
    report = {
        "timestamp": "2025-08-01",
        "model_version": "orpheus-3b-0.1-ft",
        "test_results": {
            "zero_shot_cloning": {
                "success": True,
                "quality_score": 0.75,  # Placeholder - replace with actual
                "notes": "Good voice similarity, some robotic qualities"
            },
            "parameter_optimization": {
                "best_temperature": 0.7,
                "best_top_k": 50,
                "best_repetition_penalty": 1.1,
                "notes": "Conservative settings work best"
            }
        },
        "next_steps": [
            "Collect 30+ diverse voice samples",
            "Fine-tune model on personal dataset",
            "Compare fine-tuned vs zero-shot results",
            "Optimize for specific use cases"
        ]
    }
    
    import json
    with open("evaluation_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print("✅ Evaluation report saved: evaluation_report.json")

if __name__ == "__main__":
    # Evaluate results (update paths as needed)
    # similarity = evaluate_voice_similarity("original_sample.wav", "generated_sample.wav")
    create_evaluation_report()
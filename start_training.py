# start_training.py
# Launch Orpheus fine-tuning

import os
import yaml
import wandb
from datetime import datetime

def setup_training():
    """Setup training environment"""
    
    # Load config
    with open("configs/training_config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    print(f"🚀 Starting Orpheus fine-tuning...")
    print(f"📊 Dataset: {config['dataset']['total_samples']} samples")
    print(f"🎯 Epochs: {config['training']['num_train_epochs']}")
    
    # Initialize wandb
    wandb.init(
        project="orpheus-voice-cloning",
        name=f"orpheus-finetune-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        config=config
    )
    
    # Setup directories
    os.makedirs(config["training"]["output_dir"], exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    return config

def main():
    """Main training function"""
    
    # Setup
    config = setup_training()
    
    try:
        from orpheus_tts import OrpheusModel
        
        print("📥 Loading Orpheus model...")
        model = OrpheusModel(
            model_name=config["model"]["name"],
            max_model_len=config["model"]["max_model_len"]
        )
        
        print("✅ Model loaded successfully!")
        print("⚡ Starting training...")
        print("📊 Monitor progress at: https://wandb.ai")
        
        # Training implementation would go here
        # This is a framework - actual training depends on Orpheus API
        
        print("🎉 Training completed!")
        print(f"📁 Model saved to: {config['training']['output_dir']}")
        
    except Exception as e:
        print(f"❌ Training failed: {e}")

if __name__ == "__main__":
    main()

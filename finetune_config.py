# finetune_config.py
import yaml

def create_finetune_config():
    """
    Create configuration for Orpheus fine-tuning
    """
    config = {
        "model_name": "canopylabs/orpheus-3b-0.1-pretrained",
        "dataset_path": "./voice_dataset",
        "output_dir": "./finetuned_model",
        "training_args": {
            "num_train_epochs": 3,
            "per_device_train_batch_size": 1,
            "gradient_accumulation_steps": 8,
            "learning_rate": 5e-5,
            "warmup_steps": 100,
            "logging_steps": 10,
            "save_steps": 100,
            "eval_steps": 100,
            "save_total_limit": 3,
            "prediction_loss_only": True,
            "remove_unused_columns": False,
            "fp16": True,  # Use mixed precision for memory efficiency
        },
        "generation_config": {
            "max_new_tokens": 125,  # ~10 seconds of audio
            "temperature": 0.7,
            "top_k": 50,
            "repetition_penalty": 1.1,
            "do_sample": True
        },
        "data_config": {
            "sample_rate": 24000,
            "max_duration": 15,
            "audio_column": "audio",
            "text_column": "transcript"
        }
    }
    
    with open("finetune_config.yaml", "w") as f:
        yaml.dump(config, f, default_flow_style=False)
    
    print("✅ Fine-tuning configuration created: finetune_config.yaml")
    return config

if __name__ == "__main__":
    create_finetune_config()
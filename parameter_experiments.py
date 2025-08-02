# parameter_experiments.py
import json
import time

def experiment_with_parameters():
    """
    Systematic experimentation with different parameters
    """
    print("🔬 Starting parameter experiments...")
    
    # Parameter ranges to test
    experiments = {
        "temperature_test": {
            "base_params": {"top_k": 50, "repetition_penalty": 1.1},
            "variable": "temperature",
            "values": [0.3, 0.5, 0.7, 0.9, 1.1]
        },
        "top_k_test": {
            "base_params": {"temperature": 0.7, "repetition_penalty": 1.1},
            "variable": "top_k", 
            "values": [10, 25, 50, 75, 100]
        },
        "repetition_penalty_test": {
            "base_params": {"temperature": 0.7, "top_k": 50},
            "variable": "repetition_penalty",
            "values": [1.0, 1.05, 1.1, 1.15, 1.2]
        }
    }
    
    results = {}
    test_text = "This is a parameter testing experiment for voice cloning."
    
    for exp_name, exp_config in experiments.items():
        print(f"\n📊 Running {exp_name}...")
        results[exp_name] = []
        
        for value in exp_config["values"]:
            params = exp_config["base_params"].copy()
            params[exp_config["variable"]] = value
            
            print(f"  Testing {exp_config['variable']}={value}")
            
            try:
                start_time = time.time()
                
                # Generate audio with current parameters
                # (Replace with actual Orpheus API call)
                output_file = f"experiment_{exp_name}_{exp_config['variable']}_{value}.wav"
                
                generation_time = time.time() - start_time
                
                result = {
                    "parameters": params,
                    "output_file": output_file,
                    "generation_time": generation_time,
                    "success": True
                }
                
                results[exp_name].append(result)
                print(f"    ✅ Success in {generation_time:.2f}s")
                
            except Exception as e:
                result = {
                    "parameters": params,
                    "error": str(e),
                    "success": False
                }
                results[exp_name].append(result)
                print(f"    ❌ Failed: {e}")
    
    # Save experiment results
    with open("parameter_experiments.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n📋 Experiment results saved to parameter_experiments.json")
    return results

if __name__ == "__main__":
    experiment_with_parameters()
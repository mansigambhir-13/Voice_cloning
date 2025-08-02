# system_diagnostics.py
# Check your system capabilities and suggest solutions

import torch
import sys
import platform
import subprocess

def check_system_info():
    """
    Check system configuration and GPU availability
    """
    print("🖥️  SYSTEM DIAGNOSTICS")
    print("="*50)
    
    # Basic system info
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Python Version: {sys.version}")
    print(f"PyTorch Version: {torch.__version__}")
    
    # GPU/CUDA info
    print(f"\n🎮 GPU INFORMATION:")
    print(f"CUDA Available: {torch.cuda.is_available()}")
    print(f"CUDA Version: {torch.version.cuda if torch.cuda.is_available() else 'Not available'}")
    print(f"GPU Count: {torch.cuda.device_count()}")
    
    if torch.cuda.is_available():
        for i in range(torch.cuda.device_count()):
            gpu_name = torch.cuda.get_device_name(i)
            gpu_memory = torch.cuda.get_device_properties(i).total_memory / 1e9
            print(f"  GPU {i}: {gpu_name} ({gpu_memory:.1f} GB)")
    else:
        print("  No CUDA GPUs detected")
    
    # Check if NVIDIA GPU exists (even without CUDA PyTorch)
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("  🎮 NVIDIA GPU detected (nvidia-smi works)")
            print("  💡 You have GPU hardware but PyTorch is CPU-only")
        else:
            print("  🖥️  No NVIDIA GPU or drivers detected")
    except:
        print("  🖥️  No NVIDIA GPU detected")

def check_orpheus_requirements():
    """
    Check if system meets Orpheus requirements
    """
    print("\n🔍 ORPHEUS REQUIREMENTS CHECK:")
    print("="*50)
    
    # Memory check
    try:
        import psutil
        memory_gb = psutil.virtual_memory().total / 1e9
        print(f"System RAM: {memory_gb:.1f} GB")
        
        if memory_gb >= 16:
            print("  ✅ RAM: Sufficient for Orpheus")
        elif memory_gb >= 8:
            print("  ⚠️  RAM: May work but could be slow")
        else:
            print("  ❌ RAM: May not be sufficient")
    except:
        print("  ❓ Could not check RAM")
    
    # Storage check
    import shutil
    free_space = shutil.disk_usage('.').free / 1e9
    print(f"Free Storage: {free_space:.1f} GB")
    
    if free_space >= 10:
        print("  ✅ Storage: Sufficient")
    else:
        print("  ⚠️  Storage: May need more space for models")

def suggest_solutions():
    """
    Suggest solutions based on system configuration
    """
    print("\n💡 RECOMMENDED SOLUTIONS:")
    print("="*50)
    
    if torch.cuda.is_available():
        print("🎮 You have CUDA support - great!")
        print("  Solution: Configure Orpheus to use your GPU")
    else:
        print("🖥️  CPU-only mode available")
        print("  Solution 1: Use CPU mode (slower but works)")
        print("  Solution 2: Install CUDA PyTorch for GPU acceleration")
        print("  Solution 3: Use Lightning AI cloud GPUs")
    
    print("\n📋 NEXT STEPS:")
    print("1. Try CPU mode first: python cpu_fix_test.py")
    print("2. If CPU too slow, consider GPU setup")
    print("3. Continue with Lightning AI for training")

if __name__ == "__main__":
    print("="*60)
    print("         SYSTEM DIAGNOSTICS FOR ORPHEUS TTS")
    print("="*60)
    
    check_system_info()
    check_orpheus_requirements()
    suggest_solutions()
    
    print("\n" + "="*60)
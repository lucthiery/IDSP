
try:
    from datasets import load_dataset
    ds = load_dataset("drveronika/4_x_fake_profile_detection")
    ds.save_to_disk("data/4_x_fake_profile_detection")
    print("[+] Saved Hugging Face dataset to data/4_x_fake_profile_detection")
except ImportError:
    print("[!] Hugging Face datasets library not installed. Run: pip install datasets")
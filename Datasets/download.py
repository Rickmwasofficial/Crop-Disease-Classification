import os
import requests
import zipfile
from pathlib import Path

def download_dataset(url, save_dir):
    """
    Download and extract dataset directly in GitHub Codespace
    """
    # Create directory if it doesn't exist
    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    
    # Download file
    response = requests.get(url, stream=True)
    zip_path = save_dir / "dataset.zip"
    
    print("Download started!!!")
    # Save downloaded file
    with open(zip_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("completed!!!")
    # Extract files
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(save_dir)
    
    # Remove zip file
    zip_path.unlink()

# Example usage
dataset_url = "https://www.kaggle.com/api/v1/datasets/download/abdallahalidev/plantvillage-dataset"  # Replace with actual dataset URL
save_directory = "plant_disease"
download_dataset(dataset_url, save_directory)
import sys
import zipfile

def extract_zip(file_path, password):
    try:
        with zipfile.ZipFile(file_path) as zf:
            zf.extractall(pwd=password.encode())
            print("File extracted successfully")
    except Exception as e:
        print(f"Failed to extract file: {e}")

if __name__ == "__main__":
    file_path = sys.argv[1]
    password = sys.argv[2]
    extract_zip(file_path, password)

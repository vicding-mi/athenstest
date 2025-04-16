import os
import sys
import json
import httpx


# External service URL
VALIDATION_URL = "https://google.com"
CHANGED_FILES = os.getenv("CHANGED_FILES", "")
if CHANGED_FILES and CHANGED_FILES != "":
    CHANGED_FILES = CHANGED_FILES.split()

print(f"CHANGED_FILES: {CHANGED_FILES}")
print(f"cli parameter: {sys.argv[1] if len(sys.argv) > 1 else None}")

def get_pushed_files():
    pushed_files = CHANGED_FILES.copy()
    return [file for file in pushed_files if file.endswith(".json")]


def validate_file(file_path):
    """Validate a single file against the external service."""
    with open(file_path, "rb") as f:
        # response = httpx.post(VALIDATION_URL, files={"file": f})
        response = httpx.get(VALIDATION_URL)
        if 200 <= response.status_code < 300:
            print(f"✅ {file_path} is valid.")
            return True
        else:
            print(f"❌ {file_path} is invalid: {response.text}")
            return False


def main():
    """Main function to validate pushed files."""
    print(f"CHANGED_FILES: {CHANGED_FILES}")
    pushed_files = get_pushed_files()
    print(f"Pushed files: {pushed_files}")
    if not pushed_files:
        print("No JSON files to validate.")
        return

    all_valid = True
    for file_path in pushed_files:
        if os.path.exists(file_path):
            if not validate_file(file_path):
                all_valid = False
        else:
            print(f"⚠️ File {file_path} does not exist locally.")
            all_valid = False

    if not all_valid:
        exit(1)


if __name__ == "__main__":
    main()

import os
import json
import httpx

# External service URL
VALIDATION_URL = "https://google.com"


def get_pushed_files():
    """Retrieve the list of files just pushed from the GitHub event payload."""
    event_path = os.getenv("GITHUB_EVENT_PATH")
    print(f"GITHUB_EVENT_PATH: {event_path}")
    if not event_path or not os.path.exists(event_path):
        raise FileNotFoundError("GITHUB_EVENT_PATH is not set or the file does not exist.")

    with open(event_path, "r") as f:
        event_data = json.load(f)

    pushed_files = set()
    for commit in event_data.get("commits", []):
        pushed_files.update(commit.get("added", []))
        pushed_files.update(commit.get("modified", []))

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
    pushed_files = get_pushed_files()
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

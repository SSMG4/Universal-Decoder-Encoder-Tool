import requests, os, shutil, zipfile
from io import BytesIO

REPO = "SSMG4/Universal-Decoder-Encoder-Tool"
CURRENT_VERSION = "v1.0-release"
BRANCH = "master"

def fetch_latest_commit_sha():
    url = f"https://api.github.com/repos/SSMG4/Universal-Decoder-Encoder-Tool/commits/master"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['sha']
    return None

def update_tool():
    print("[*] Downloading latest source from main branch...")
    zip_url = f"https://github.com/SSMG4/Universal-Decoder-Encoder-Tool/archive/refs/heads/master.zip"
    r = requests.get(zip_url)
    with zipfile.ZipFile(BytesIO(r.content)) as z:
        temp_dir = "_update_temp"
        z.extractall(temp_dir)

        folder = next(os.walk(temp_dir))[1][0]
        update_path = os.path.join(temp_dir, folder)

        for item in os.listdir(update_path):
            s = os.path.join(update_path, item)
            d = os.path.join(".", item)
            if os.path.isdir(s):
                if os.path.exists(d): shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)

        shutil.rmtree(temp_dir)
        print("[+] Update complete! Restart the tool to apply changes.")

def main():
    print("[*] Checking for updates...")
    local_sha_path = ".current_commit"
    latest_sha = fetch_latest_commit_sha()

    if not latest_sha:
        print("[-] Could not fetch latest commit SHA.")
        return

    if os.path.exists(local_sha_path):
        with open(local_sha_path) as f:
            current_sha = f.read().strip()
    else:
        current_sha = "unknown"

    if current_sha != latest_sha:
        print(f"[!] Update available (commit: {latest_sha[:7]})")
        choice = input("Update now? (Y/n): ").lower()
        if choice in ["y", ""]:
            update_tool()
            with open(local_sha_path, "w") as f:
                f.write(latest_sha)
        else:
            print("[*] Update canceled.")
    else:
        print("[✓] You're already up to date!")

if __name__ == "__main__":
    main()

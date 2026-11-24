"""The long roast: lawmakers and the file they cannot convert.

Writes one satirical sentence to /output/entry.txt (deterministic, stdlib only).
"""

import os

ROAST = "They spent three hours debating how to regulate the cloud in a room with a fax machine, then asked an intern to print the internet so they could read it, and now they want to legislate a file format they could not convert if their own re-election depended on it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    print(f"wrote /output/entry.txt ({len(ROAST)} characters)")

if __name__ == "__main__":
    main()

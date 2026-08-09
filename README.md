# 🦆 Pond-Purge: The Music Library Canonicalizer

**Pond-Purge** is a high-integrity media management suite designed to rescue music libraries from "subfolder hell." It transforms a fragmented collection of files scattered across multiple USB drives, external TB disks, and messy download folders into a single, deduplicated, and tagged canonical library.

Unlike simple "copy-paste" methods, Pond-Purge uses **cryptographic hashing (SHA-256)** to ensure that no matter how many times a song appears across your drives, it only occupies one spot in your final nest.

---

## 🛠 The Pipeline

The system operates in two distinct phases:

### Phase 1: The Migration (`build_music_library.py`)
**Goal:** Ingest files from various sources and consolidate them into a master "MUSIC" directory.
- **Content-Addressable Storage:** Every file is hashed. If the hash exists in the manifest, the file is skipped.
- **Source Agnostic:** Can loop through any number of mount points (e.g., `/mnt/chromeos/removable/*`).
- **Manifest Tracking:** Maintains a `music_manifest.json` which acts as the "Source of Truth" for the entire library.

### Phase 2: The Grooming (`cleanup_music_library.py`)
**Goal:** Polish the consolidated library and remove debris.
- **Junk Removal:** Wipes `.ds_store`, `thumbs.db`, and incomplete `.part` or `.crdownload` files.
- **Integrity Check:** Identifies "broken" audio files (zero-byte or unparseable) and removes them.
- **Metadata Recovery:** Uses the folder hierarchy (`Artist/Album/Track`) and filename patterns to fill in missing ID3 tags.
- **Directory Pruning:** Recursively deletes empty folders left behind after the cleaning pass.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.8+**
- **Mutagen** (for audio metadata handling):
  ```bash
  pip install mutagen
  ```

### Installation
```bash
git clone https://github.com/yourusername/pond-purge.git
cd pond-purge
```

---

## 📖 Usage Guide

### 1. Building the Library
To consolidate files from multiple drives into your main Music folder:

```bash
# Single drive run
python3 build_music_library.py --root /path/to/source --dest ~/Music --manifest ~/music_manifest.json --execute

# Bulk run across all removable drives (Linux/ChromeOS)
for vol in /mnt/chromeos/removable/*/; do
  python3 build_music_library.py --root "$vol" --dest ~/Music --manifest ~/music_manifest.json --execute
done
```

### 2. Cleaning the Library
Always run the cleaner in **Report-Only** mode first to see what will be deleted.

```bash
# Dry Run (Safe)
python3 cleanup_music_library.py --music-dir ~/Music --manifest ~/music_manifest.json

# Full Execution (Permanent)
python3 cleanup_music_library.py --music-dir ~/Music --manifest ~/music_manifest.json --execute
```

---

## ⚙️ Technical Specifications

### SHA-256 Hashing Logic
To avoid loading multi-gigabyte files into RAM, the system reads files in **64KB chunks**. This ensures the script remains lightweight even when processing FLAC albums or high-res WAV files.

### Tag-Fix Heuristics
The `cleanup` script employs a regex-based parser to recover track info from filenames:
- **Pattern:** `^\s*(\d{1,3})[\s\-\._]+(.*)$`
- **Example:** `01 - Moonlight Sonata.mp3` $\rightarrow$ **Track:** `01`, **Title:** `Moonlight Sonata`.

### Arguments Table

| Flag | Script | Description | Default |
| :--- | :--- | :--- | :--- |
| `--root` | Build | The source directory to scan. | N/A |
| `--dest` | Build | Where the canonical files will live. | `~/Music` |
| `--manifest` | Both | Path to the JSON tracking file. | `~/music_manifest.json` |
| `--music-dir` | Clean | The directory to be pruned/fixed. | `~/Music` |
| `--execute` | Both | If omitted, script runs in **Dry Run** mode. | `False` |

---

## 🛡 OPSEC & Safety
- **No-Overwrite Policy:** The builder checks the manifest before moving any file, preventing accidental overwrites of better-tagged versions.
- **Dry-Run First:** The `cleanup` script defaults to report-only mode. **Never** run with `--execute` until you have reviewed the scan results.
- **Non-Destructive Ingestion:** The builder *copies* files; it does not move them from the source drives, ensuring your original backups remain intact.

---

## 🦆 Carter's Duck-Tips
- **Slow Drives:** If you are scanning a mechanical HDD, expect SHA-256 to take some time. It's not hung; it's just swimming through a lot of data!
- **Cover Art:** The script is configured to keep `.jpg`, `.png`, and `.webp` files—don't let the cleaner wipe your album art!
- **Manifest Loss:** If you lose your `music_manifest.json`, you can simply re-run the build script; it will re-hash the library and rebuild the manifest.
-adjust screen settings and turn computer going to sleep off for the 1st scan

**Quack! Happy organizing!** 🦆


🐸 Pond-Purge (v0.9.0-beta)Deterministic Music Ingestion, Deduplication, Tag Inference, and Grooming Toolkit.pond-purge brings order to chaotic music directories. It provides a robust, two-phase engine that ingests unorganized audio files into a clean ~/Music/Artist/Album/Track - Title.ext layout, deduplicates content via SHA-256 chunked hashing, fixes incomplete audio metadata tags, and prunes directory cruft safely.📁 Repository Structurepond-purge/
├── .github/
│   └── workflows/
│       └── python-tests.yml      # Automated pytest CI workflow
├── docs/
│   ├── architecture.md           # SHA-256 pipeline & module spec
│   └── user-guide.md             # In-depth CLI options & examples
├── tests/
│   ├── __init__.py
│   ├── test_hashing.py           # Unit tests for SHA-256 & broken file checks
│   └── test_tagging.py           # Unit tests for filename regex & tag parsing
├── src/
│   ├── __init__.py
│   ├── build_music_library.py    # The Ingestion Engine
│   └── cleanup_music_library.py  # The Grooming Engine
├── .gitignore                    # Python & local workspace filters
├── LICENSE                       # MIT License
├── project.json                  # Project metadata
├── README.md                     # Main repository guide
└── requirements.txt              # Mutagen & Pytest dependencies
⚡ Quick Start1. Ingest Unorganized AudioScan a download or raw folder and migrate non-duplicate tracks to your canonical music directory:# Report-only preview
python3 src/build_music_library.py --source ~/Downloads/Unorganized

# Perform migration and create manifest
python3 src/build_music_library.py --source ~/Downloads/Unorganized --execute
2. Groom & Clean LibraryPerform a comprehensive 5-pass health check across your ~/Music tree:# Report-only dry run
python3 src/cleanup_music_library.py

# Execute cleanup pass
python3 src/cleanup_music_library.py --execute
🧪 Running Unit TestsRun the unit test suite locally with pytest:pytest --verbose tests/
🛡️ Key Features & Safety RulesContent-Based Deduplication: Identifies duplicate tracks by cryptographic hash rather than filename.Dry-Run Safety: Default execution mode is always REPORT-ONLY. Changes require --execute.Cover Art Preservation: Album art (.jpg, .png, .webp) is whitelisted and untouched.ID3/Vorbis/MP4 Tag Repair: Automatically infers missing fields from directory hierarchy and writes tags back into track headers.

import pytest
from pathlib import Path
from src.build_music_library import sha256_of, AUDIO_EXTS
from src.cleanup_music_library import is_broken_audio


def test_sha256_calculation(tmp_path: Path):
    test_file = tmp_path / "test.mp3"
    content = b"PondPurgeTestDataContent12345"
    test_file.write_bytes(content)

    import hashlib
    expected_hash = hashlib.sha256(content).hexdigest()
    assert sha256_of(test_file) == expected_hash


def test_zero_byte_file_detection(tmp_path: Path):
    empty_file = tmp_path / "empty.flac"
    empty_file.write_bytes(b"")

    assert is_broken_audio(empty_file) is True


def test_audio_extensions_whitelist():
    assert ".mp3" in AUDIO_EXTS
    assert ".flac" in AUDIO_EXTS
    assert ".m4a" in AUDIO_EXTS
    assert ".txt" not in AUDIO_EXTS
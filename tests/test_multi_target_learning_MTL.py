"""Test module for multi_target_learning_MTL."""

from multi_target_learning_MTL import __author__, __email__, __version__


def test_project_info():
    """Test __author__ value."""
    assert __author__ == "Panos Kazantzis"
    assert __email__ == "p.kazantzis@yahoo.com"
    assert __version__ == "0.0.0"

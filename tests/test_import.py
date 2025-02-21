"""Test uvtestbtn."""

import uvtestbtn


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(uvtestbtn.__name__, str)

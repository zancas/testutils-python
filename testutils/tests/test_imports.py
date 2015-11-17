import mock
import pytest

@pytest.mark.usefixtures("return_mock_imports")
class TestImports:
    # (Class Level) Multi-test fixture setup, stuff that needs to be in a known fresh state at the beginning of multiple tests
    import_names_to_mock = ['choice']
    import_modules_to_mock = ['math']

    def test_import_mocker(self):
        # Test setup specific to this test regime
        import imports
        # Run the specific test

        # Evaluate/verify results
        assert isinstance(imports.choice, mock.MagicMock)
        assert isinstance(imports.math, mock.MagicMock)

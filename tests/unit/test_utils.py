import pytest
from deepclassifier.utils import read_yaml
from box import ConfigBox
from pathlib import Path
from ensure.main import EnsureError

class Test_read_yaml:
    yaml_files = [
        "tests/data/empty_for_test.yaml",
        "tests/data/dummy_for_test.yaml"
    ]

    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):
            read_yaml(Path(self.yaml_files[0]))

    def test_read_yaml_return_type(self):
        respone = read_yaml(Path(self.yaml_files[-1]))
        assert isinstance(respone, ConfigBox)

    @pytest.mark.parametrize("path_to_yaml", yaml_files)
    def test_read_yaml_bad_type(self, path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)
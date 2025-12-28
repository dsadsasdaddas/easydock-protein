"""
测试配置文件

配置pytest和Hypothesis的全局设置。
"""

import pytest
from hypothesis import settings, Verbosity

# 配置Hypothesis全局设置
settings.register_profile("default", max_examples=100, verbosity=Verbosity.verbose)
settings.register_profile("ci", max_examples=1000, verbosity=Verbosity.normal)
settings.register_profile("dev", max_examples=10, verbosity=Verbosity.verbose)

# 使用默认配置
settings.load_profile("default")


@pytest.fixture(scope="session")
def test_data_dir():
    """测试数据目录fixture"""
    import os
    return os.path.join(os.path.dirname(__file__), "data")


@pytest.fixture
def sample_protein_sequence():
    """示例蛋白质序列fixture"""
    return "MKWVTFISLLLLFSSAYSRGVFRRDTHKSEIAHRFKDLGEEHFKGLVLIAFSQYLQQCPFDEHVKLVNELTEFAKTCVADESHAGCEKSLHTLFGDELCKVASLRETYGDMADCCEKQEPERNECFLSHKDDSPDLPKLKPDPNTLCDEFKADEKKFWGKYLYEIARRHPYFYAPELLYYANKYNGVFQECCQAEDKGACLLPKIETMREKVLASSARQRLRCASIQKFGERALKAWSVARLSQKFPKAEFVEVTKLVTDLTKVHKECCHGDLLECADDRADLAKYICDNQDTISSKLKECCDKPVNGFNLCF"


@pytest.fixture
def sample_pdb_data():
    """示例PDB数据fixture"""
    return """HEADER    TRANSFERASE                             01-JAN-00   1ABC              
ATOM      1  N   ALA A   1      20.154  16.967  14.421  1.00 20.00           N  
ATOM      2  CA  ALA A   1      19.030  16.101  14.421  1.00 20.00           C  
ATOM      3  C   ALA A   1      17.693  16.849  14.421  1.00 20.00           C  
ATOM      4  O   ALA A   1      17.693  18.079  14.421  1.00 20.00           O  
ATOM      5  CB  ALA A   1      19.030  15.188  13.207  1.00 20.00           C  
END"""
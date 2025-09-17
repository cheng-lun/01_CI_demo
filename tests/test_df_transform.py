from pathlib import Path
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from lib import df_transform

test_path = Path(__file__).parent
golden_input = test_path / "golden_input" / "golden_input.xlsx"

CASES = [
    ("add_new_column", df_transform.add_new_column, test_path / "golden_output" / "df_new_col.xlsx"),
    ("reverse_columns", df_transform.reverse_columns, test_path / "golden_output" / "df_reversed.xlsx"),
]

@pytest.mark.parametrize("name,function,output_excel", CASES, ids=[case[0] for case in CASES])
def test_df(name, function, output_excel):
    df_golden_input = pd.read_excel(golden_input)
    golden_output = function(df_golden_input)
    output_df = pd.read_excel(output_excel)
    assert_frame_equal(golden_output, output_df, check_dtype=True, check_exact=True)
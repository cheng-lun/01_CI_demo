import pandas as pd

def add_new_column(df):
    df_new_col = df.copy()
    df_new_col['new_column'] = 'test'

    return df_new_col


def reverse_columns(df):
    df = df.copy()
    df_reversed = df[df.columns[::-1]].copy()

    return df_reversed


if __name__ == '__main__':
    df = pd.read_excel('../tests/golden_input/golden_input.xlsx')
    df_new_col = add_new_column(df)
    df_reversed = reverse_columns(df)
    df_new_col.to_excel('df_new_col.xlsx', index = False)
    df_reversed.to_excel('df_reversed.xlsx', index=False)

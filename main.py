#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:           main.py
Author:         Antonio Arteaga
Last Updated:   2025-02-03
Version:        1.0
Description:    DataFrames are obtained from CSV files, they are cleaned and 
                transformed, finally, all DataFrames are loaded to SQL Server (ETL).
Dependencies:   polars==1.38.1, openpyxl==3.1.5, xlsxwriter==3.2.9, pyarrow==23.0.1,
Usage:          CSV files are requested to run this script.
"""

from pkg.extract import *
from pkg.transform import *
from pkg.load import *


def main():
    """E-T-L process."""
    for table_name in TABLES_TO_PROCESS:
        print("\n" + "=" * 25)
        print(f"📊 Procesando tabla: {table_name}")
        print("=" * 25)
        try:
            # 1. Extraction (E)
            df = extract_from_file(table_name, ROOT_PATH)
            # df_sample_raw = df.sample(100, seed=42)
            # df_sample_raw.write_excel(f'{table_name}_sample_raw.xlsx')
            # """
            # 2. Transformation (T)
            df_trans = transform(df, table_name)
            """
            df_sample = df_trans.sample(10, seed=42)
            try:
                df_sample.write_excel(f'{table_name}_clean.xlsx')
            except:
                print("\n\nNo puedo escribir en el excel si está abierto!")
            """
            # 3. Load to SQL Server (L)
            load_table(df_trans, f'{table_name}')
            # """
        except Exception as e:
            print(
                f"\n❌ FALLO CRÍTICO para {table_name}.\n")
            print(f"'{e}'")
            print("=" * 25)

    print("\n--- PROCESO FINALIZADO ---")


if __name__ == '__main__':
    main()

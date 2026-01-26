

from pkg.extract import *
from pkg.transform import *


def main():
    """E-T-L pipeline."""
    for table_name in TABLES_TO_PROCESS:
        print("\n" + "=" * 25)
        print(f"| 📊 Procesando Tabla: {table_name}")
        print("=" * 25)
        try:
            # 1. Extraction (E)
            df = extract_from_file(table_name, ROOT_DATA_PATH)
            # df_sample_raw = df.sample(100, seed=42)
            # df_sample_raw.write_excel(f'{table_name}_sample_raw.xlsx')

            # 2. Transformation (T)
            df_trans = transform(df)
            df_sample = df_trans.sample(1000, seed=42)
            try:
                df_sample.write_excel(f'{table_name}_clean.xlsx')
            except:
                print("\n\nNo puedo escribir en el excel si está abierto!")

            # 3. Load to SQL Server (L)
            df = df.head(10)
            index_load_table(df, f'{table_name}_clean')

        except Exception as e:
            print(
                f"\n❌ FALLO CRÍTICO para {table_name}. Mensaje:\n")
            print(f"'{e}'")
            print("=" * 25)

    print("\n--- PIPELINE COMPLETO FINALIZADO ---")


if __name__ == '__main__':
    main()

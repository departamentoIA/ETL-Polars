# main.py
from pkg.funciones import crear_dataframe_ejemplo, subir_a_sql_y_indexar


def main():
    print("Iniciando proceso...")

    # Crear los datos
    df = crear_dataframe_ejemplo()
    print("DataFrame creado localmente:")
    print(df.head())

    # Ejecutar carga y optimización
    subir_a_sql_y_indexar(df)

    print("Proceso finalizado con éxito.")


if __name__ == "__main__":
    main()

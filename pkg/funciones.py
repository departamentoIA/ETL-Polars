# modules.py
import polars as pl
import datetime
from sqlalchemy import create_engine
from pkg.config import get_connection_string

TABLE_NAME = 'polars_table'


def crear_dataframe_ejemplo():
    """Crea un DataFrame de 10 filas con tipos de datos específicos."""
    datos = {
        "fecha": [datetime.date(2024, 1, i+1) for i in range(10)],
        "id_cadena": [f"ID-{i:03}" for i in range(10)],
        "entero_32": [i * 10 for i in range(10)],
        "flotante": [i * 1.5 for i in range(10)]
    }

    # Forzamos los tipos de datos en Polars
    return pl.DataFrame(datos).with_columns([
        pl.col("fecha").cast(pl.Datetime),
        pl.col("id_cadena").cast(pl.String),
        pl.col("entero_32").cast(pl.Int32),
        pl.col("flotante").cast(pl.Float64)
    ])


def subir_a_sql_y_indexar(df: pl.DataFrame):
    """Sube el DataFrame usando SQLAlchemy y crea el índice."""

    # 1. Crear el motor de SQLAlchemy
    # fast_executemany=True es el secreto de la velocidad en SQL Server
    engine = create_engine(get_connection_string(), fast_executemany=True)

    try:
        # Polars detectará el motor de SQLAlchemy automáticamente
        df.write_database(
            table_name=TABLE_NAME,
            connection=engine,
            if_table_exists="fail"
        )
        print(f"✓ Datos subidos exitosamente a {TABLE_NAME}")
        """
        # 2. Crear Índice / Primary Key
        with engine.begin() as conn:
            # SQL Server requiere que la PK no sea nula y tenga tamaño definido
            conn.exec_driver_sql(
                f"ALTER TABLE {TABLE_NAME} ALTER COLUMN id_cadena NVARCHAR(50) NOT NULL")
            conn.exec_driver_sql(
                f"ALTER TABLE {TABLE_NAME} ADD PRIMARY KEY (id_cadena)")
            print(f"✓ Primary Key creada en 'id_cadena'")
        """
    except Exception as e:
        print(f"❌ Error: {e}")

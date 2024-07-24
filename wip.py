from sqlalchemy import create_engine

engine = create_engine(

    # 'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'

    'sqlite:///database.db', echo=True  # criando um bd em memória
)


print(engine.pool)

con = engine.connect()

print(engine.pool.status())
# print(con.connection.dbapi_connection)

con.close()

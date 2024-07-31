import sqlalchemy as sa
from sqlalchemy import engine, insert,

metadata = sa.MetaData()

engine = sa.create_engine('sqlite:///database.db')

# t = sa.Table(
#     'comments',
#     metadata,
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('name', sa.String(), nullable=False),
#     sa.Column('comment', sa.String(), nullable=False),
#     sa.Column('created_at', sa.DateTime(), nullable=False),
#     sa.PrimaryKeyConstraint('id'),

# )
t = sa.Table('comments', metadata, autoload_with=engine)

sql = insert(t).values(
    name='regi',
    comment='é isso aí',

)

print(sql)

# with engine.connect() as con:
#     result = con.execute(sql)
#     print(result.fetchmany(10))  # Seleciona os 10 primeiros valores

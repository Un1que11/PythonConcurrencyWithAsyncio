import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='localhost',
                                       port=5432,
                                       user='postgres',
                                       password='password',
                                       database='products')
    async with connection.transaction():
        await connection.execute("INSERT INTO brand "
                                 "VALUES (DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand "
                                 "VALUES (DEFAULT, 'brand_2')")

    query = """SELECT brand_name FROM brand
                WHERE brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


asyncio.run(main())

import asyncio
import logging
import asyncpg


async def main():
    connection = await asyncpg.connect(host='localhost',
                                       port=5432,
                                       user='postgres',
                                       password='password',
                                       database='products')
    try:
        async with connection.transaction():
            await connection.execute("INSERT INTO brand "
                                     "VALUES (9999, 'big_brand')")
            await connection.execute("INSERT INTO brand "
                                     "VALUES (9999, 'big_brand')")
    except Exception as e:
        logging.exception(e)
    finally:
        query = """SELECT brand_name FROM brand
                    WHERE brand_name LIKE 'big_%'"""
        brands = await connection.fetch(query)
        print(brands)

    await connection.close()


asyncio.run(main())

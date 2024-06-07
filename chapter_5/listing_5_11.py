import asyncio
import logging
import asyncpg


async def main():
    connection = await asyncpg.connect(host='localhost',
                                       port=5432,
                                       user='postgres',
                                       password='password',
                                       database='products')
    async with connection.transaction():
        await connection.execute("INSERT INTO brand "
                                 "VALUES (DEFAULT, 'my_new_brand')")

        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color "
                                         "VALUES (1, 'black')")
        except Exception as ex:
            logging.warning('Ignoring error inserting product color',
                            exc_info=ex)

    await connection.close()


asyncio.run(main())

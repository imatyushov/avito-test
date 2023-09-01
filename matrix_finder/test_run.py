import asyncio

from httpx import AsyncClient

from matrix_finder import get_raw_http_result


async def main():
    url = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
    bytes_content = get_raw_http_result(url, AsyncClient())
    print(bytes_content)

if __name__ == '__main__':
    asyncio.run(main())
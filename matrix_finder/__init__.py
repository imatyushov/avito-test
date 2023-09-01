from httpx import AsyncClient

from matrix_finder.utils import get_raw_http_result


def create_matrix_from_bytes(bytes_content):
    pass


def traverse_matrix(matrix):
    pass


async def get_matrix(url: str) -> list[int]:
    bytes_content = await get_raw_http_result(url, AsyncClient())
    matrix = await create_matrix_from_bytes(bytes_content)

    return await traverse_matrix(matrix)



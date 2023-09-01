from httpx import AsyncClient, TimeoutException, ProtocolError

from http.client import HTTPException


async def get_raw_http_result(url: str, http_client: AsyncClient):
    try:
        response = await http_client.get(url)
    except TimeoutException:
        raise HTTPException(f'Не удалось получить ответ от "{url}" ')
    except ProtocolError:
        raise HTTPException(f'Некорректно указан "{url}"')

    if response.is_error:
        raise HTTPException(f'Сервер ответил с ошибкой, статус коды 400, 500. url: {url}. Текст ошибки: {response.content}')

    return response.content



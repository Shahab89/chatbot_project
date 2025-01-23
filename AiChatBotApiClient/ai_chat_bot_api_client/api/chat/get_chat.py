from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_chat_response_dto import GetChatResponseDto
from ...types import Response


def _get_kwargs(
    chat_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/chats/{chat_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetChatResponseDto]:
    if response.status_code == 200:
        response_200 = GetChatResponseDto.from_dict(response.text)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetChatResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetChatResponseDto]:
    """
    Args:
        chat_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetChatResponseDto]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetChatResponseDto]:
    """
    Args:
        chat_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetChatResponseDto
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    chat_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetChatResponseDto]:
    """
    Args:
        chat_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetChatResponseDto]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetChatResponseDto]:
    """
    Args:
        chat_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetChatResponseDto
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
        )
    ).parsed

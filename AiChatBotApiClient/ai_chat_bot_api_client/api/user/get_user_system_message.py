from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_system_message_response_dto import GetUserSystemMessageResponseDto
from ...types import Response


def _get_kwargs(
    user_system_message_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/users/current/userSystemMessage/{user_system_message_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetUserSystemMessageResponseDto]:
    if response.status_code == 200:
        response_200 = GetUserSystemMessageResponseDto.from_dict(response.text)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetUserSystemMessageResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_system_message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetUserSystemMessageResponseDto]:
    """
    Args:
        user_system_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserSystemMessageResponseDto]
    """

    kwargs = _get_kwargs(
        user_system_message_id=user_system_message_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_system_message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetUserSystemMessageResponseDto]:
    """
    Args:
        user_system_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserSystemMessageResponseDto
    """

    return sync_detailed(
        user_system_message_id=user_system_message_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_system_message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetUserSystemMessageResponseDto]:
    """
    Args:
        user_system_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserSystemMessageResponseDto]
    """

    kwargs = _get_kwargs(
        user_system_message_id=user_system_message_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_system_message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetUserSystemMessageResponseDto]:
    """
    Args:
        user_system_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserSystemMessageResponseDto
    """

    return (
        await asyncio_detailed(
            user_system_message_id=user_system_message_id,
            client=client,
        )
    ).parsed

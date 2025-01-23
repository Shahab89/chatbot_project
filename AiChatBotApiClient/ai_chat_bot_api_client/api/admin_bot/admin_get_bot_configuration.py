from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_get_bot_configuration_response_dto import AdminGetBotConfigurationResponseDto
from ...types import Response


def _get_kwargs(
    bot_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/admin/bots/{bot_id}/configuration",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AdminGetBotConfigurationResponseDto]:
    if response.status_code == 200:
        response_200 = AdminGetBotConfigurationResponseDto.from_dict(response.text)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AdminGetBotConfigurationResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AdminGetBotConfigurationResponseDto]:
    """
    Args:
        bot_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminGetBotConfigurationResponseDto]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AdminGetBotConfigurationResponseDto]:
    """
    Args:
        bot_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminGetBotConfigurationResponseDto
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AdminGetBotConfigurationResponseDto]:
    """
    Args:
        bot_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminGetBotConfigurationResponseDto]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AdminGetBotConfigurationResponseDto]:
    """
    Args:
        bot_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminGetBotConfigurationResponseDto
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_create_bot_fact_request_dto import AdminCreateBotFactRequestDto
from ...models.admin_create_bot_fact_response_dto import AdminCreateBotFactResponseDto
from ...types import Response


def _get_kwargs(
    bot_id: str,
    *,
    body: Union[
        AdminCreateBotFactRequestDto,
        AdminCreateBotFactRequestDto,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/admin/bots/{bot_id}/facts",
    }

    if isinstance(body, AdminCreateBotFactRequestDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, AdminCreateBotFactRequestDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AdminCreateBotFactResponseDto]:
    if response.status_code == 200:
        response_200 = AdminCreateBotFactResponseDto.from_dict(response.text)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AdminCreateBotFactResponseDto]:
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
    body: Union[
        AdminCreateBotFactRequestDto,
        AdminCreateBotFactRequestDto,
    ],
) -> Response[AdminCreateBotFactResponseDto]:
    """
    Args:
        bot_id (str):
        body (AdminCreateBotFactRequestDto):
        body (AdminCreateBotFactRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminCreateBotFactResponseDto]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AdminCreateBotFactRequestDto,
        AdminCreateBotFactRequestDto,
    ],
) -> Optional[AdminCreateBotFactResponseDto]:
    """
    Args:
        bot_id (str):
        body (AdminCreateBotFactRequestDto):
        body (AdminCreateBotFactRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminCreateBotFactResponseDto
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AdminCreateBotFactRequestDto,
        AdminCreateBotFactRequestDto,
    ],
) -> Response[AdminCreateBotFactResponseDto]:
    """
    Args:
        bot_id (str):
        body (AdminCreateBotFactRequestDto):
        body (AdminCreateBotFactRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminCreateBotFactResponseDto]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AdminCreateBotFactRequestDto,
        AdminCreateBotFactRequestDto,
    ],
) -> Optional[AdminCreateBotFactResponseDto]:
    """
    Args:
        bot_id (str):
        body (AdminCreateBotFactRequestDto):
        body (AdminCreateBotFactRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminCreateBotFactResponseDto
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
            body=body,
        )
    ).parsed

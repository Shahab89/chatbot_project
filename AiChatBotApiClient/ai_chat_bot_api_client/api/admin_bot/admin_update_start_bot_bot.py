from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_update_start_bot_bot_request_dto import AdminUpdateStartBotBotRequestDto
from ...types import Response


def _get_kwargs(
    start_bot_id: str,
    bot_id: str,
    *,
    body: Union[
        AdminUpdateStartBotBotRequestDto,
        AdminUpdateStartBotBotRequestDto,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/admin/bots/{start_bot_id}/bots/{bot_id}",
    }

    if isinstance(body, AdminUpdateStartBotBotRequestDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, AdminUpdateStartBotBotRequestDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    start_bot_id: str,
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AdminUpdateStartBotBotRequestDto,
        AdminUpdateStartBotBotRequestDto,
    ],
) -> Response[Any]:
    """
    Args:
        start_bot_id (str):
        bot_id (str):
        body (AdminUpdateStartBotBotRequestDto):
        body (AdminUpdateStartBotBotRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_bot_id=start_bot_id,
        bot_id=bot_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    start_bot_id: str,
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AdminUpdateStartBotBotRequestDto,
        AdminUpdateStartBotBotRequestDto,
    ],
) -> Response[Any]:
    """
    Args:
        start_bot_id (str):
        bot_id (str):
        body (AdminUpdateStartBotBotRequestDto):
        body (AdminUpdateStartBotBotRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_bot_id=start_bot_id,
        bot_id=bot_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

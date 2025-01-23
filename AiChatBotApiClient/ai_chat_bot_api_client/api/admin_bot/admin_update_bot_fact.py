from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_update_bot_fact_request_dto import AdminUpdateBotFactRequestDto
from ...types import Response


def _get_kwargs(
    bot_id: str,
    bot_fact_id: str,
    *,
    body: Union[
        AdminUpdateBotFactRequestDto,
        AdminUpdateBotFactRequestDto,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/admin/bots/{bot_id}/facts/{bot_fact_id}",
    }

    if isinstance(body, AdminUpdateBotFactRequestDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, AdminUpdateBotFactRequestDto):
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
    bot_id: str,
    bot_fact_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AdminUpdateBotFactRequestDto,
        AdminUpdateBotFactRequestDto,
    ],
) -> Response[Any]:
    """
    Args:
        bot_id (str):
        bot_fact_id (str):
        body (AdminUpdateBotFactRequestDto):
        body (AdminUpdateBotFactRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        bot_fact_id=bot_fact_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    bot_id: str,
    bot_fact_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AdminUpdateBotFactRequestDto,
        AdminUpdateBotFactRequestDto,
    ],
) -> Response[Any]:
    """
    Args:
        bot_id (str):
        bot_fact_id (str):
        body (AdminUpdateBotFactRequestDto):
        body (AdminUpdateBotFactRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        bot_fact_id=bot_fact_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

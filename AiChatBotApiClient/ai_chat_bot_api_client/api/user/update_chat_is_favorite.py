from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_update_is_favorite_request_dto import ChatUpdateIsFavoriteRequestDto
from ...types import Response


def _get_kwargs(
    chatid: str,
    *,
    body: Union[
        ChatUpdateIsFavoriteRequestDto,
        ChatUpdateIsFavoriteRequestDto,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/users/current/chats/{chatid}/isfavorite",
    }

    if isinstance(body, ChatUpdateIsFavoriteRequestDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ChatUpdateIsFavoriteRequestDto):
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
    chatid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ChatUpdateIsFavoriteRequestDto,
        ChatUpdateIsFavoriteRequestDto,
    ],
) -> Response[Any]:
    """
    Args:
        chatid (str):
        body (ChatUpdateIsFavoriteRequestDto):
        body (ChatUpdateIsFavoriteRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chatid=chatid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    chatid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ChatUpdateIsFavoriteRequestDto,
        ChatUpdateIsFavoriteRequestDto,
    ],
) -> Response[Any]:
    """
    Args:
        chatid (str):
        body (ChatUpdateIsFavoriteRequestDto):
        body (ChatUpdateIsFavoriteRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chatid=chatid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_completion_request_dto import ChatCompletionRequestDto
from ...models.chat_completion_response_dto import ChatCompletionResponseDto
from ...types import Response


def _get_kwargs(
    chat_id: str,
    *,
    body: Union[
        ChatCompletionRequestDto,
        ChatCompletionRequestDto,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/chats/{chat_id}/completions",
    }

    if isinstance(body, ChatCompletionRequestDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ChatCompletionRequestDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ChatCompletionResponseDto]:
    if response.status_code == 200:
        response_200 = ChatCompletionResponseDto(response.text)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ChatCompletionResponseDto]:
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
    body: Union[
        ChatCompletionRequestDto,
        ChatCompletionRequestDto,
    ],
) -> Response[ChatCompletionResponseDto]:
    """
    Args:
        chat_id (str):
        body (ChatCompletionRequestDto):
        body (ChatCompletionRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatCompletionResponseDto]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ChatCompletionRequestDto,
        ChatCompletionRequestDto,
    ],
) -> Optional[ChatCompletionResponseDto]:
    """
    Args:
        chat_id (str):
        body (ChatCompletionRequestDto):
        body (ChatCompletionRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatCompletionResponseDto
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    chat_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ChatCompletionRequestDto,
        ChatCompletionRequestDto,
    ],
) -> Response[ChatCompletionResponseDto]:
    """
    Args:
        chat_id (str):
        body (ChatCompletionRequestDto):
        body (ChatCompletionRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatCompletionResponseDto]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ChatCompletionRequestDto,
        ChatCompletionRequestDto,
    ],
) -> Optional[ChatCompletionResponseDto]:
    """
    Args:
        chat_id (str):
        body (ChatCompletionRequestDto):
        body (ChatCompletionRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatCompletionResponseDto
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
            body=body,
        )
    ).parsed

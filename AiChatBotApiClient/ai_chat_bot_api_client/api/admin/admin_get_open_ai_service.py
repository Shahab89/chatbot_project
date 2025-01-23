from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_get_open_ai_service_response_dto import AdminGetOpenAiServiceResponseDto
from ...types import Response


def _get_kwargs(
    open_ai_service_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/admin/openAiServices/{open_ai_service_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AdminGetOpenAiServiceResponseDto]:
    if response.status_code == 200:
        response_200 = AdminGetOpenAiServiceResponseDto.from_dict(response.text)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AdminGetOpenAiServiceResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    open_ai_service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AdminGetOpenAiServiceResponseDto]:
    """
    Args:
        open_ai_service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminGetOpenAiServiceResponseDto]
    """

    kwargs = _get_kwargs(
        open_ai_service_id=open_ai_service_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    open_ai_service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AdminGetOpenAiServiceResponseDto]:
    """
    Args:
        open_ai_service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminGetOpenAiServiceResponseDto
    """

    return sync_detailed(
        open_ai_service_id=open_ai_service_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    open_ai_service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AdminGetOpenAiServiceResponseDto]:
    """
    Args:
        open_ai_service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminGetOpenAiServiceResponseDto]
    """

    kwargs = _get_kwargs(
        open_ai_service_id=open_ai_service_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    open_ai_service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AdminGetOpenAiServiceResponseDto]:
    """
    Args:
        open_ai_service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminGetOpenAiServiceResponseDto
    """

    return (
        await asyncio_detailed(
            open_ai_service_id=open_ai_service_id,
            client=client,
        )
    ).parsed

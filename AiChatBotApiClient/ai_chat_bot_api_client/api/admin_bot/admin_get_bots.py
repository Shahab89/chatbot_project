from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_get_bots_response_item_dto_paging_result import AdminGetBotsResponseItemDtoPagingResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["SearchFor"] = search_for

    params["OrderBy"] = order_by

    params["PageNumber"] = page_number

    params["PageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/bots",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AdminGetBotsResponseItemDtoPagingResult]:
    if response.status_code == 200:
        response_200 = AdminGetBotsResponseItemDtoPagingResult.from_dict(response.text)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AdminGetBotsResponseItemDtoPagingResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[AdminGetBotsResponseItemDtoPagingResult]:
    """
    Args:
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminGetBotsResponseItemDtoPagingResult]
    """

    kwargs = _get_kwargs(
        search_for=search_for,
        order_by=order_by,
        page_number=page_number,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[AdminGetBotsResponseItemDtoPagingResult]:
    """
    Args:
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminGetBotsResponseItemDtoPagingResult
    """

    return sync_detailed(
        client=client,
        search_for=search_for,
        order_by=order_by,
        page_number=page_number,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[AdminGetBotsResponseItemDtoPagingResult]:
    """
    Args:
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminGetBotsResponseItemDtoPagingResult]
    """

    kwargs = _get_kwargs(
        search_for=search_for,
        order_by=order_by,
        page_number=page_number,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[AdminGetBotsResponseItemDtoPagingResult]:
    """
    Args:
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminGetBotsResponseItemDtoPagingResult
    """

    return (
        await asyncio_detailed(
            client=client,
            search_for=search_for,
            order_by=order_by,
            page_number=page_number,
            page_size=page_size,
        )
    ).parsed

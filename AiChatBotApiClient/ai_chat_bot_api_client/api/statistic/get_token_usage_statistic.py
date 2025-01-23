import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_token_usage_statistic_response_item_dto_paging_result import (
    GetTokenUsageStatisticResponseItemDtoPagingResult,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bot_id: Union[Unset, str] = UNSET,
    token_usage_type_id: Union[Unset, int] = UNSET,
    from_request_date: Union[Unset, datetime.date] = UNSET,
    to_request_date: Union[Unset, datetime.date] = UNSET,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["BotId"] = bot_id

    params["TokenUsageTypeId"] = token_usage_type_id

    json_from_request_date: Union[Unset, str] = UNSET
    if not isinstance(from_request_date, Unset):
        json_from_request_date = from_request_date.isoformat()
    params["FromRequestDate"] = json_from_request_date

    json_to_request_date: Union[Unset, str] = UNSET
    if not isinstance(to_request_date, Unset):
        json_to_request_date = to_request_date.isoformat()
    params["ToRequestDate"] = json_to_request_date

    params["SearchFor"] = search_for

    params["OrderBy"] = order_by

    params["PageNumber"] = page_number

    params["PageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/statistic/tokenUsageStatistic",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetTokenUsageStatisticResponseItemDtoPagingResult]:
    if response.status_code == 200:
        response_200 = GetTokenUsageStatisticResponseItemDtoPagingResult.from_dict(response.text)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetTokenUsageStatisticResponseItemDtoPagingResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    bot_id: Union[Unset, str] = UNSET,
    token_usage_type_id: Union[Unset, int] = UNSET,
    from_request_date: Union[Unset, datetime.date] = UNSET,
    to_request_date: Union[Unset, datetime.date] = UNSET,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[GetTokenUsageStatisticResponseItemDtoPagingResult]:
    """
    Args:
        bot_id (Union[Unset, str]):
        token_usage_type_id (Union[Unset, int]):
        from_request_date (Union[Unset, datetime.date]):
        to_request_date (Union[Unset, datetime.date]):
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTokenUsageStatisticResponseItemDtoPagingResult]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        token_usage_type_id=token_usage_type_id,
        from_request_date=from_request_date,
        to_request_date=to_request_date,
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
    bot_id: Union[Unset, str] = UNSET,
    token_usage_type_id: Union[Unset, int] = UNSET,
    from_request_date: Union[Unset, datetime.date] = UNSET,
    to_request_date: Union[Unset, datetime.date] = UNSET,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[GetTokenUsageStatisticResponseItemDtoPagingResult]:
    """
    Args:
        bot_id (Union[Unset, str]):
        token_usage_type_id (Union[Unset, int]):
        from_request_date (Union[Unset, datetime.date]):
        to_request_date (Union[Unset, datetime.date]):
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTokenUsageStatisticResponseItemDtoPagingResult
    """

    return sync_detailed(
        client=client,
        bot_id=bot_id,
        token_usage_type_id=token_usage_type_id,
        from_request_date=from_request_date,
        to_request_date=to_request_date,
        search_for=search_for,
        order_by=order_by,
        page_number=page_number,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    bot_id: Union[Unset, str] = UNSET,
    token_usage_type_id: Union[Unset, int] = UNSET,
    from_request_date: Union[Unset, datetime.date] = UNSET,
    to_request_date: Union[Unset, datetime.date] = UNSET,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[GetTokenUsageStatisticResponseItemDtoPagingResult]:
    """
    Args:
        bot_id (Union[Unset, str]):
        token_usage_type_id (Union[Unset, int]):
        from_request_date (Union[Unset, datetime.date]):
        to_request_date (Union[Unset, datetime.date]):
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTokenUsageStatisticResponseItemDtoPagingResult]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        token_usage_type_id=token_usage_type_id,
        from_request_date=from_request_date,
        to_request_date=to_request_date,
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
    bot_id: Union[Unset, str] = UNSET,
    token_usage_type_id: Union[Unset, int] = UNSET,
    from_request_date: Union[Unset, datetime.date] = UNSET,
    to_request_date: Union[Unset, datetime.date] = UNSET,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[GetTokenUsageStatisticResponseItemDtoPagingResult]:
    """
    Args:
        bot_id (Union[Unset, str]):
        token_usage_type_id (Union[Unset, int]):
        from_request_date (Union[Unset, datetime.date]):
        to_request_date (Union[Unset, datetime.date]):
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTokenUsageStatisticResponseItemDtoPagingResult
    """

    return (
        await asyncio_detailed(
            client=client,
            bot_id=bot_id,
            token_usage_type_id=token_usage_type_id,
            from_request_date=from_request_date,
            to_request_date=to_request_date,
            search_for=search_for,
            order_by=order_by,
            page_number=page_number,
            page_size=page_size,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_get_bot_feedback_response_item_dto_paging_result import (
    AdminGetBotFeedbackResponseItemDtoPagingResult,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_id: str,
    *,
    filter_by_vote: Union[Unset, int] = UNSET,
    show_feedbacks_without_status: Union[Unset, bool] = UNSET,
    show_feedbacks_with_status: Union[Unset, bool] = UNSET,
    filter_by_status: Union[Unset, int] = UNSET,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["FilterByVote"] = filter_by_vote

    params["ShowFeedbacksWithoutStatus"] = show_feedbacks_without_status

    params["ShowFeedbacksWithStatus"] = show_feedbacks_with_status

    params["FilterByStatus"] = filter_by_status

    params["SearchFor"] = search_for

    params["OrderBy"] = order_by

    params["PageNumber"] = page_number

    params["PageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/admin/bots/{bot_id}/feedback",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AdminGetBotFeedbackResponseItemDtoPagingResult]:
    if response.status_code == 200:
        response_200 = AdminGetBotFeedbackResponseItemDtoPagingResult.from_dict(response.text)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AdminGetBotFeedbackResponseItemDtoPagingResult]:
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
    filter_by_vote: Union[Unset, int] = UNSET,
    show_feedbacks_without_status: Union[Unset, bool] = UNSET,
    show_feedbacks_with_status: Union[Unset, bool] = UNSET,
    filter_by_status: Union[Unset, int] = UNSET,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[AdminGetBotFeedbackResponseItemDtoPagingResult]:
    """
    Args:
        bot_id (str):
        filter_by_vote (Union[Unset, int]):
        show_feedbacks_without_status (Union[Unset, bool]):
        show_feedbacks_with_status (Union[Unset, bool]):
        filter_by_status (Union[Unset, int]):
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminGetBotFeedbackResponseItemDtoPagingResult]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        filter_by_vote=filter_by_vote,
        show_feedbacks_without_status=show_feedbacks_without_status,
        show_feedbacks_with_status=show_feedbacks_with_status,
        filter_by_status=filter_by_status,
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
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_by_vote: Union[Unset, int] = UNSET,
    show_feedbacks_without_status: Union[Unset, bool] = UNSET,
    show_feedbacks_with_status: Union[Unset, bool] = UNSET,
    filter_by_status: Union[Unset, int] = UNSET,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[AdminGetBotFeedbackResponseItemDtoPagingResult]:
    """
    Args:
        bot_id (str):
        filter_by_vote (Union[Unset, int]):
        show_feedbacks_without_status (Union[Unset, bool]):
        show_feedbacks_with_status (Union[Unset, bool]):
        filter_by_status (Union[Unset, int]):
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminGetBotFeedbackResponseItemDtoPagingResult
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        filter_by_vote=filter_by_vote,
        show_feedbacks_without_status=show_feedbacks_without_status,
        show_feedbacks_with_status=show_feedbacks_with_status,
        filter_by_status=filter_by_status,
        search_for=search_for,
        order_by=order_by,
        page_number=page_number,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_by_vote: Union[Unset, int] = UNSET,
    show_feedbacks_without_status: Union[Unset, bool] = UNSET,
    show_feedbacks_with_status: Union[Unset, bool] = UNSET,
    filter_by_status: Union[Unset, int] = UNSET,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[AdminGetBotFeedbackResponseItemDtoPagingResult]:
    """
    Args:
        bot_id (str):
        filter_by_vote (Union[Unset, int]):
        show_feedbacks_without_status (Union[Unset, bool]):
        show_feedbacks_with_status (Union[Unset, bool]):
        filter_by_status (Union[Unset, int]):
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminGetBotFeedbackResponseItemDtoPagingResult]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        filter_by_vote=filter_by_vote,
        show_feedbacks_without_status=show_feedbacks_without_status,
        show_feedbacks_with_status=show_feedbacks_with_status,
        filter_by_status=filter_by_status,
        search_for=search_for,
        order_by=order_by,
        page_number=page_number,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_by_vote: Union[Unset, int] = UNSET,
    show_feedbacks_without_status: Union[Unset, bool] = UNSET,
    show_feedbacks_with_status: Union[Unset, bool] = UNSET,
    filter_by_status: Union[Unset, int] = UNSET,
    search_for: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[AdminGetBotFeedbackResponseItemDtoPagingResult]:
    """
    Args:
        bot_id (str):
        filter_by_vote (Union[Unset, int]):
        show_feedbacks_without_status (Union[Unset, bool]):
        show_feedbacks_with_status (Union[Unset, bool]):
        filter_by_status (Union[Unset, int]):
        search_for (Union[Unset, str]):
        order_by (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminGetBotFeedbackResponseItemDtoPagingResult
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
            filter_by_vote=filter_by_vote,
            show_feedbacks_without_status=show_feedbacks_without_status,
            show_feedbacks_with_status=show_feedbacks_with_status,
            filter_by_status=filter_by_status,
            search_for=search_for,
            order_by=order_by,
            page_number=page_number,
            page_size=page_size,
        )
    ).parsed

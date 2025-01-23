import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTokenUsageStatisticResponseItemDto")


@_attrs_define
class GetTokenUsageStatisticResponseItemDto:
    """
    Attributes:
        request_date (Union[Unset, datetime.date]):
        bot_id (Union[None, Unset, str]):
        bot_display_name (Union[None, Unset, str]):
        token_usage_type_id (Union[Unset, int]):
        user_count (Union[Unset, int]):
        request_count (Union[Unset, int]):
        prompt_tokens (Union[Unset, int]):
        completion_tokens (Union[Unset, int]):
        total_tokens (Union[Unset, int]):
    """

    request_date: Union[Unset, datetime.date] = UNSET
    bot_id: Union[None, Unset, str] = UNSET
    bot_display_name: Union[None, Unset, str] = UNSET
    token_usage_type_id: Union[Unset, int] = UNSET
    user_count: Union[Unset, int] = UNSET
    request_count: Union[Unset, int] = UNSET
    prompt_tokens: Union[Unset, int] = UNSET
    completion_tokens: Union[Unset, int] = UNSET
    total_tokens: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        request_date: Union[Unset, str] = UNSET
        if not isinstance(self.request_date, Unset):
            request_date = self.request_date.isoformat()

        bot_id: Union[None, Unset, str]
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        bot_display_name: Union[None, Unset, str]
        if isinstance(self.bot_display_name, Unset):
            bot_display_name = UNSET
        else:
            bot_display_name = self.bot_display_name

        token_usage_type_id = self.token_usage_type_id

        user_count = self.user_count

        request_count = self.request_count

        prompt_tokens = self.prompt_tokens

        completion_tokens = self.completion_tokens

        total_tokens = self.total_tokens

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if request_date is not UNSET:
            field_dict["requestDate"] = request_date
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if bot_display_name is not UNSET:
            field_dict["botDisplayName"] = bot_display_name
        if token_usage_type_id is not UNSET:
            field_dict["tokenUsageTypeId"] = token_usage_type_id
        if user_count is not UNSET:
            field_dict["userCount"] = user_count
        if request_count is not UNSET:
            field_dict["requestCount"] = request_count
        if prompt_tokens is not UNSET:
            field_dict["promptTokens"] = prompt_tokens
        if completion_tokens is not UNSET:
            field_dict["completionTokens"] = completion_tokens
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _request_date = d.pop("requestDate", UNSET)
        request_date: Union[Unset, datetime.date]
        if isinstance(_request_date, Unset):
            request_date = UNSET
        else:
            request_date = isoparse(_request_date).date()

        def _parse_bot_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_id = _parse_bot_id(d.pop("botId", UNSET))

        def _parse_bot_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_display_name = _parse_bot_display_name(d.pop("botDisplayName", UNSET))

        token_usage_type_id = d.pop("tokenUsageTypeId", UNSET)

        user_count = d.pop("userCount", UNSET)

        request_count = d.pop("requestCount", UNSET)

        prompt_tokens = d.pop("promptTokens", UNSET)

        completion_tokens = d.pop("completionTokens", UNSET)

        total_tokens = d.pop("totalTokens", UNSET)

        get_token_usage_statistic_response_item_dto = cls(
            request_date=request_date,
            bot_id=bot_id,
            bot_display_name=bot_display_name,
            token_usage_type_id=token_usage_type_id,
            user_count=user_count,
            request_count=request_count,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=total_tokens,
        )

        return get_token_usage_statistic_response_item_dto

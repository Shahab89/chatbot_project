from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserRequestDto")


@_attrs_define
class UpdateUserRequestDto:
    """
    Attributes:
        is_keep_chat_history (Union[Unset, bool]):
        keep_chat_history_for_days (Union[Unset, int]):
        is_keep_favorites_forever (Union[Unset, bool]):
    """

    is_keep_chat_history: Union[Unset, bool] = UNSET
    keep_chat_history_for_days: Union[Unset, int] = UNSET
    is_keep_favorites_forever: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_keep_chat_history = self.is_keep_chat_history

        keep_chat_history_for_days = self.keep_chat_history_for_days

        is_keep_favorites_forever = self.is_keep_favorites_forever

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_keep_chat_history is not UNSET:
            field_dict["isKeepChatHistory"] = is_keep_chat_history
        if keep_chat_history_for_days is not UNSET:
            field_dict["keepChatHistoryForDays"] = keep_chat_history_for_days
        if is_keep_favorites_forever is not UNSET:
            field_dict["isKeepFavoritesForever"] = is_keep_favorites_forever

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_keep_chat_history = d.pop("isKeepChatHistory", UNSET)

        keep_chat_history_for_days = d.pop("keepChatHistoryForDays", UNSET)

        is_keep_favorites_forever = d.pop("isKeepFavoritesForever", UNSET)

        update_user_request_dto = cls(
            is_keep_chat_history=is_keep_chat_history,
            keep_chat_history_for_days=keep_chat_history_for_days,
            is_keep_favorites_forever=is_keep_favorites_forever,
        )

        return update_user_request_dto

import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetChatsResponseItemDto")


@_attrs_define
class GetChatsResponseItemDto:
    """
    Attributes:
        chat_id (Union[None, Unset, str]):
        display_name (Union[None, Unset, str]):
        last_accessed_utc (Union[Unset, datetime.datetime]):
        bot_id (Union[None, Unset, str]):
        bot_display_name (Union[None, Unset, str]):
        user_system_message_id (Union[None, Unset, str]):
        user_system_message_display_name (Union[None, Unset, str]):
        is_favorite (Union[Unset, bool]):
    """

    chat_id: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    last_accessed_utc: Union[Unset, datetime.datetime] = UNSET
    bot_id: Union[None, Unset, str] = UNSET
    bot_display_name: Union[None, Unset, str] = UNSET
    user_system_message_id: Union[None, Unset, str] = UNSET
    user_system_message_display_name: Union[None, Unset, str] = UNSET
    is_favorite: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        chat_id: Union[None, Unset, str]
        if isinstance(self.chat_id, Unset):
            chat_id = UNSET
        else:
            chat_id = self.chat_id

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        last_accessed_utc: Union[Unset, str] = UNSET
        if not isinstance(self.last_accessed_utc, Unset):
            last_accessed_utc = self.last_accessed_utc.isoformat()

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

        user_system_message_id: Union[None, Unset, str]
        if isinstance(self.user_system_message_id, Unset):
            user_system_message_id = UNSET
        else:
            user_system_message_id = self.user_system_message_id

        user_system_message_display_name: Union[None, Unset, str]
        if isinstance(self.user_system_message_display_name, Unset):
            user_system_message_display_name = UNSET
        else:
            user_system_message_display_name = self.user_system_message_display_name

        is_favorite = self.is_favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if last_accessed_utc is not UNSET:
            field_dict["lastAccessedUtc"] = last_accessed_utc
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if bot_display_name is not UNSET:
            field_dict["botDisplayName"] = bot_display_name
        if user_system_message_id is not UNSET:
            field_dict["userSystemMessageId"] = user_system_message_id
        if user_system_message_display_name is not UNSET:
            field_dict["userSystemMessageDisplayName"] = user_system_message_display_name
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_chat_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chat_id = _parse_chat_id(d.pop("chatId", UNSET))

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        _last_accessed_utc = d.pop("lastAccessedUtc", UNSET)
        last_accessed_utc: Union[Unset, datetime.datetime]
        if isinstance(_last_accessed_utc, Unset):
            last_accessed_utc = UNSET
        else:
            last_accessed_utc = isoparse(_last_accessed_utc)

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

        def _parse_user_system_message_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_system_message_id = _parse_user_system_message_id(d.pop("userSystemMessageId", UNSET))

        def _parse_user_system_message_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_system_message_display_name = _parse_user_system_message_display_name(
            d.pop("userSystemMessageDisplayName", UNSET)
        )

        is_favorite = d.pop("isFavorite", UNSET)

        get_chats_response_item_dto = cls(
            chat_id=chat_id,
            display_name=display_name,
            last_accessed_utc=last_accessed_utc,
            bot_id=bot_id,
            bot_display_name=bot_display_name,
            user_system_message_id=user_system_message_id,
            user_system_message_display_name=user_system_message_display_name,
            is_favorite=is_favorite,
        )

        return get_chats_response_item_dto

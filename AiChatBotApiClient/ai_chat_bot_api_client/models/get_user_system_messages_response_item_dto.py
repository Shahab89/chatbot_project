from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserSystemMessagesResponseItemDto")


@_attrs_define
class GetUserSystemMessagesResponseItemDto:
    """
    Attributes:
        user_system_message_id (Union[None, Unset, str]):
        display_name (Union[None, Unset, str]):
    """

    user_system_message_id: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_system_message_id: Union[None, Unset, str]
        if isinstance(self.user_system_message_id, Unset):
            user_system_message_id = UNSET
        else:
            user_system_message_id = self.user_system_message_id

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_system_message_id is not UNSET:
            field_dict["userSystemMessageId"] = user_system_message_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_user_system_message_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_system_message_id = _parse_user_system_message_id(d.pop("userSystemMessageId", UNSET))

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        get_user_system_messages_response_item_dto = cls(
            user_system_message_id=user_system_message_id,
            display_name=display_name,
        )

        return get_user_system_messages_response_item_dto

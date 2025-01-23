from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOpenChatBotIdResponseDto")


@_attrs_define
class GetOpenChatBotIdResponseDto:
    """
    Attributes:
        open_chat_bot_id (Union[None, Unset, str]):
        is_public (Union[Unset, bool]):
    """

    open_chat_bot_id: Union[None, Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        open_chat_bot_id: Union[None, Unset, str]
        if isinstance(self.open_chat_bot_id, Unset):
            open_chat_bot_id = UNSET
        else:
            open_chat_bot_id = self.open_chat_bot_id

        is_public = self.is_public

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if open_chat_bot_id is not UNSET:
            field_dict["openChatBotId"] = open_chat_bot_id
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_open_chat_bot_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        open_chat_bot_id = _parse_open_chat_bot_id(d.pop("openChatBotId", UNSET))

        is_public = d.pop("isPublic", UNSET)

        get_open_chat_bot_id_response_dto = cls(
            open_chat_bot_id=open_chat_bot_id,
            is_public=is_public,
        )

        return get_open_chat_bot_id_response_dto

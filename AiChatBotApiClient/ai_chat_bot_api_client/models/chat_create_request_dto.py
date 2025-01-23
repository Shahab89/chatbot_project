from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCreateRequestDto")


@_attrs_define
class ChatCreateRequestDto:
    """
    Attributes:
        bot_id (Union[None, Unset, str]):
    """

    bot_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bot_id: Union[None, Unset, str]
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_bot_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_id = _parse_bot_id(d.pop("botId", UNSET))

        chat_create_request_dto = cls(
            bot_id=bot_id,
        )
        print("✅ chat_create_request_dto:", chat_create_request_dto)

        return chat_create_request_dto

from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCreateByBotCodeRequestDto")


@_attrs_define
class ChatCreateByBotCodeRequestDto:
    """
    Attributes:
        bot_code (Union[None, Unset, str]):
    """

    bot_code: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bot_code: Union[None, Unset, str]
        if isinstance(self.bot_code, Unset):
            bot_code = UNSET
        else:
            bot_code = self.bot_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bot_code is not UNSET:
            field_dict["botCode"] = bot_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_bot_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_code = _parse_bot_code(d.pop("botCode", UNSET))

        chat_create_by_bot_code_request_dto = cls(
            bot_code=bot_code,
        )

        return chat_create_by_bot_code_request_dto

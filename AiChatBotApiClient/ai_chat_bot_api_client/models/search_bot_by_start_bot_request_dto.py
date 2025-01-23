from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchBotByStartBotRequestDto")


@_attrs_define
class SearchBotByStartBotRequestDto:
    """
    Attributes:
        user_message (Union[None, Unset, str]):
    """

    user_message: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_message: Union[None, Unset, str]
        if isinstance(self.user_message, Unset):
            user_message = UNSET
        else:
            user_message = self.user_message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_message is not UNSET:
            field_dict["userMessage"] = user_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_user_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_message = _parse_user_message(d.pop("userMessage", UNSET))

        search_bot_by_start_bot_request_dto = cls(
            user_message=user_message,
        )

        return search_bot_by_start_bot_request_dto

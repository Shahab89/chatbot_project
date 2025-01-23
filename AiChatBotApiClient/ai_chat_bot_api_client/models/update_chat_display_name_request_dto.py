from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateChatDisplayNameRequestDto")


@_attrs_define
class UpdateChatDisplayNameRequestDto:
    """
    Attributes:
        display_name (Union[None, Unset, str]):
    """

    display_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        update_chat_display_name_request_dto = cls(
            display_name=display_name,
        )

        return update_chat_display_name_request_dto

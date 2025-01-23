from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserSystemMessageCountResponseDto")


@_attrs_define
class GetUserSystemMessageCountResponseDto:
    """
    Attributes:
        system_message_count (Union[Unset, int]):
    """

    system_message_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        system_message_count = self.system_message_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if system_message_count is not UNSET:
            field_dict["systemMessageCount"] = system_message_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        system_message_count = d.pop("systemMessageCount", UNSET)

        get_user_system_message_count_response_dto = cls(
            system_message_count=system_message_count,
        )

        return get_user_system_message_count_response_dto

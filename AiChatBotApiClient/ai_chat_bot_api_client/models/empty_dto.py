from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="EmptyDto")


@_attrs_define
class EmptyDto:
    """ """

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        empty_dto = cls()

        return empty_dto

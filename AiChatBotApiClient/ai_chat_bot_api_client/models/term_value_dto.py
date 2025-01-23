from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TermValueDto")


@_attrs_define
class TermValueDto:
    """
    Attributes:
        value (Union[None, Unset, str]):
        value_de (Union[None, Unset, str]):
    """

    value: Union[None, Unset, str] = UNSET
    value_de: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        value_de: Union[None, Unset, str]
        if isinstance(self.value_de, Unset):
            value_de = UNSET
        else:
            value_de = self.value_de

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if value_de is not UNSET:
            field_dict["valueDe"] = value_de

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_value_de(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value_de = _parse_value_de(d.pop("valueDe", UNSET))

        term_value_dto = cls(
            value=value,
            value_de=value_de,
        )

        return term_value_dto

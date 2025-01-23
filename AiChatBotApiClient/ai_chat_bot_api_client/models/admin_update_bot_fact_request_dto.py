from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminUpdateBotFactRequestDto")


@_attrs_define
class AdminUpdateBotFactRequestDto:
    """
    Attributes:
        is_active (Union[Unset, bool]):
        fact_text (Union[None, Unset, str]):
    """

    is_active: Union[Unset, bool] = UNSET
    fact_text: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_active = self.is_active

        fact_text: Union[None, Unset, str]
        if isinstance(self.fact_text, Unset):
            fact_text = UNSET
        else:
            fact_text = self.fact_text

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if fact_text is not UNSET:
            field_dict["factText"] = fact_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_active = d.pop("isActive", UNSET)

        def _parse_fact_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fact_text = _parse_fact_text(d.pop("factText", UNSET))

        admin_update_bot_fact_request_dto = cls(
            is_active=is_active,
            fact_text=fact_text,
        )

        return admin_update_bot_fact_request_dto

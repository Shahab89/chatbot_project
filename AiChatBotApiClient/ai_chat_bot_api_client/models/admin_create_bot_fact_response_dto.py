from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminCreateBotFactResponseDto")


@_attrs_define
class AdminCreateBotFactResponseDto:
    """
    Attributes:
        bot_fact_id (Union[None, Unset, str]):
    """

    bot_fact_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bot_fact_id: Union[None, Unset, str]
        if isinstance(self.bot_fact_id, Unset):
            bot_fact_id = UNSET
        else:
            bot_fact_id = self.bot_fact_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bot_fact_id is not UNSET:
            field_dict["botFactId"] = bot_fact_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_bot_fact_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_fact_id = _parse_bot_fact_id(d.pop("botFactId", UNSET))

        admin_create_bot_fact_response_dto = cls(
            bot_fact_id=bot_fact_id,
        )

        return admin_create_bot_fact_response_dto

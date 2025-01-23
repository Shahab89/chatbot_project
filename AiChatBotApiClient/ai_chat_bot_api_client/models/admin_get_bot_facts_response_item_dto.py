import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminGetBotFactsResponseItemDto")


@_attrs_define
class AdminGetBotFactsResponseItemDto:
    """
    Attributes:
        bot_fact_id (Union[None, Unset, str]):
        is_active (Union[Unset, bool]):
        fact_text (Union[None, Unset, str]):
        created_utc (Union[Unset, datetime.datetime]):
        updated_utc (Union[Unset, datetime.datetime]):
    """

    bot_fact_id: Union[None, Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    fact_text: Union[None, Unset, str] = UNSET
    created_utc: Union[Unset, datetime.datetime] = UNSET
    updated_utc: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bot_fact_id: Union[None, Unset, str]
        if isinstance(self.bot_fact_id, Unset):
            bot_fact_id = UNSET
        else:
            bot_fact_id = self.bot_fact_id

        is_active = self.is_active

        fact_text: Union[None, Unset, str]
        if isinstance(self.fact_text, Unset):
            fact_text = UNSET
        else:
            fact_text = self.fact_text

        created_utc: Union[Unset, str] = UNSET
        if not isinstance(self.created_utc, Unset):
            created_utc = self.created_utc.isoformat()

        updated_utc: Union[Unset, str] = UNSET
        if not isinstance(self.updated_utc, Unset):
            updated_utc = self.updated_utc.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bot_fact_id is not UNSET:
            field_dict["botFactId"] = bot_fact_id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if fact_text is not UNSET:
            field_dict["factText"] = fact_text
        if created_utc is not UNSET:
            field_dict["createdUtc"] = created_utc
        if updated_utc is not UNSET:
            field_dict["updatedUtc"] = updated_utc

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

        is_active = d.pop("isActive", UNSET)

        def _parse_fact_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fact_text = _parse_fact_text(d.pop("factText", UNSET))

        _created_utc = d.pop("createdUtc", UNSET)
        created_utc: Union[Unset, datetime.datetime]
        if isinstance(_created_utc, Unset):
            created_utc = UNSET
        else:
            created_utc = isoparse(_created_utc)

        _updated_utc = d.pop("updatedUtc", UNSET)
        updated_utc: Union[Unset, datetime.datetime]
        if isinstance(_updated_utc, Unset):
            updated_utc = UNSET
        else:
            updated_utc = isoparse(_updated_utc)

        admin_get_bot_facts_response_item_dto = cls(
            bot_fact_id=bot_fact_id,
            is_active=is_active,
            fact_text=fact_text,
            created_utc=created_utc,
            updated_utc=updated_utc,
        )

        return admin_get_bot_facts_response_item_dto

from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminUpdateStartBotBotRequestDto")


@_attrs_define
class AdminUpdateStartBotBotRequestDto:
    """
    Attributes:
        is_default_bot (Union[Unset, bool]):
        keywords (Union[None, Unset, str]):
    """

    is_default_bot: Union[Unset, bool] = UNSET
    keywords: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_default_bot = self.is_default_bot

        keywords: Union[None, Unset, str]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        else:
            keywords = self.keywords

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_default_bot is not UNSET:
            field_dict["isDefaultBot"] = is_default_bot
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_default_bot = d.pop("isDefaultBot", UNSET)

        def _parse_keywords(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        admin_update_start_bot_bot_request_dto = cls(
            is_default_bot=is_default_bot,
            keywords=keywords,
        )

        return admin_update_start_bot_bot_request_dto

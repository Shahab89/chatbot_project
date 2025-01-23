from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminGetUnassignedBotsResponseItemDto")


@_attrs_define
class AdminGetUnassignedBotsResponseItemDto:
    """
    Attributes:
        bot_id (Union[None, Unset, str]):
        bot_display_name (Union[None, Unset, str]):
    """

    bot_id: Union[None, Unset, str] = UNSET
    bot_display_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bot_id: Union[None, Unset, str]
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        bot_display_name: Union[None, Unset, str]
        if isinstance(self.bot_display_name, Unset):
            bot_display_name = UNSET
        else:
            bot_display_name = self.bot_display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if bot_display_name is not UNSET:
            field_dict["botDisplayName"] = bot_display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_bot_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_id = _parse_bot_id(d.pop("botId", UNSET))

        def _parse_bot_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_display_name = _parse_bot_display_name(d.pop("botDisplayName", UNSET))

        admin_get_unassigned_bots_response_item_dto = cls(
            bot_id=bot_id,
            bot_display_name=bot_display_name,
        )

        return admin_get_unassigned_bots_response_item_dto

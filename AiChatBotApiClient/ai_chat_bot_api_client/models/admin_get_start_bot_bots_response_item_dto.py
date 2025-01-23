from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminGetStartBotBotsResponseItemDto")


@_attrs_define
class AdminGetStartBotBotsResponseItemDto:
    """
    Attributes:
        bot_id (Union[None, Unset, str]):
        bot_code (Union[None, Unset, str]):
        bot_display_name (Union[None, Unset, str]):
        bot_display_message (Union[None, Unset, str]):
        bot_description (Union[None, Unset, str]):
        is_default_bot (Union[Unset, bool]):
        is_start_bot (Union[Unset, bool]):
        keywords (Union[None, Unset, str]):
    """

    bot_id: Union[None, Unset, str] = UNSET
    bot_code: Union[None, Unset, str] = UNSET
    bot_display_name: Union[None, Unset, str] = UNSET
    bot_display_message: Union[None, Unset, str] = UNSET
    bot_description: Union[None, Unset, str] = UNSET
    is_default_bot: Union[Unset, bool] = UNSET
    is_start_bot: Union[Unset, bool] = UNSET
    keywords: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bot_id: Union[None, Unset, str]
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        bot_code: Union[None, Unset, str]
        if isinstance(self.bot_code, Unset):
            bot_code = UNSET
        else:
            bot_code = self.bot_code

        bot_display_name: Union[None, Unset, str]
        if isinstance(self.bot_display_name, Unset):
            bot_display_name = UNSET
        else:
            bot_display_name = self.bot_display_name

        bot_display_message: Union[None, Unset, str]
        if isinstance(self.bot_display_message, Unset):
            bot_display_message = UNSET
        else:
            bot_display_message = self.bot_display_message

        bot_description: Union[None, Unset, str]
        if isinstance(self.bot_description, Unset):
            bot_description = UNSET
        else:
            bot_description = self.bot_description

        is_default_bot = self.is_default_bot

        is_start_bot = self.is_start_bot

        keywords: Union[None, Unset, str]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        else:
            keywords = self.keywords

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if bot_code is not UNSET:
            field_dict["botCode"] = bot_code
        if bot_display_name is not UNSET:
            field_dict["botDisplayName"] = bot_display_name
        if bot_display_message is not UNSET:
            field_dict["botDisplayMessage"] = bot_display_message
        if bot_description is not UNSET:
            field_dict["botDescription"] = bot_description
        if is_default_bot is not UNSET:
            field_dict["isDefaultBot"] = is_default_bot
        if is_start_bot is not UNSET:
            field_dict["isStartBot"] = is_start_bot
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

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

        def _parse_bot_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_code = _parse_bot_code(d.pop("botCode", UNSET))

        def _parse_bot_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_display_name = _parse_bot_display_name(d.pop("botDisplayName", UNSET))

        def _parse_bot_display_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_display_message = _parse_bot_display_message(d.pop("botDisplayMessage", UNSET))

        def _parse_bot_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_description = _parse_bot_description(d.pop("botDescription", UNSET))

        is_default_bot = d.pop("isDefaultBot", UNSET)

        is_start_bot = d.pop("isStartBot", UNSET)

        def _parse_keywords(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        admin_get_start_bot_bots_response_item_dto = cls(
            bot_id=bot_id,
            bot_code=bot_code,
            bot_display_name=bot_display_name,
            bot_display_message=bot_display_message,
            bot_description=bot_description,
            is_default_bot=is_default_bot,
            is_start_bot=is_start_bot,
            keywords=keywords,
        )

        return admin_get_start_bot_bots_response_item_dto

import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBotsResponseItemDto")


@_attrs_define
class GetBotsResponseItemDto:
    """
    Attributes:
        bot_id (Union[None, Unset, str]):
        code (Union[None, Unset, str]):
        display_name (Union[None, Unset, str]):
        display_message (Union[None, Unset, str]):
        sample_question_1 (Union[None, Unset, str]):
        sample_question_2 (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        model_name (Union[None, Unset, str]):
        is_start_bot (Union[Unset, bool]):
        created_utc (Union[Unset, datetime.datetime]):
        updated_utc (Union[Unset, datetime.datetime]):
    """

    bot_id: Union[None, Unset, str] = UNSET
    code: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    display_message: Union[None, Unset, str] = UNSET
    sample_question_1: Union[None, Unset, str] = UNSET
    sample_question_2: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    model_name: Union[None, Unset, str] = UNSET
    is_start_bot: Union[Unset, bool] = UNSET
    created_utc: Union[Unset, datetime.datetime] = UNSET
    updated_utc: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bot_id: Union[None, Unset, str]
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        display_message: Union[None, Unset, str]
        if isinstance(self.display_message, Unset):
            display_message = UNSET
        else:
            display_message = self.display_message

        sample_question_1: Union[None, Unset, str]
        if isinstance(self.sample_question_1, Unset):
            sample_question_1 = UNSET
        else:
            sample_question_1 = self.sample_question_1

        sample_question_2: Union[None, Unset, str]
        if isinstance(self.sample_question_2, Unset):
            sample_question_2 = UNSET
        else:
            sample_question_2 = self.sample_question_2

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        model_name: Union[None, Unset, str]
        if isinstance(self.model_name, Unset):
            model_name = UNSET
        else:
            model_name = self.model_name

        is_start_bot = self.is_start_bot

        created_utc: Union[Unset, str] = UNSET
        if not isinstance(self.created_utc, Unset):
            created_utc = self.created_utc.isoformat()

        updated_utc: Union[Unset, str] = UNSET
        if not isinstance(self.updated_utc, Unset):
            updated_utc = self.updated_utc.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if code is not UNSET:
            field_dict["code"] = code
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_message is not UNSET:
            field_dict["displayMessage"] = display_message
        if sample_question_1 is not UNSET:
            field_dict["sampleQuestion1"] = sample_question_1
        if sample_question_2 is not UNSET:
            field_dict["sampleQuestion2"] = sample_question_2
        if description is not UNSET:
            field_dict["description"] = description
        if model_name is not UNSET:
            field_dict["modelName"] = model_name
        if is_start_bot is not UNSET:
            field_dict["isStartBot"] = is_start_bot
        if created_utc is not UNSET:
            field_dict["createdUtc"] = created_utc
        if updated_utc is not UNSET:
            field_dict["updatedUtc"] = updated_utc

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

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_display_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_message = _parse_display_message(d.pop("displayMessage", UNSET))

        def _parse_sample_question_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sample_question_1 = _parse_sample_question_1(d.pop("sampleQuestion1", UNSET))

        def _parse_sample_question_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sample_question_2 = _parse_sample_question_2(d.pop("sampleQuestion2", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_model_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_name = _parse_model_name(d.pop("modelName", UNSET))

        is_start_bot = d.pop("isStartBot", UNSET)

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

        get_bots_response_item_dto = cls(
            bot_id=bot_id,
            code=code,
            display_name=display_name,
            display_message=display_message,
            sample_question_1=sample_question_1,
            sample_question_2=sample_question_2,
            description=description,
            model_name=model_name,
            is_start_bot=is_start_bot,
            created_utc=created_utc,
            updated_utc=updated_utc,
        )

        return get_bots_response_item_dto

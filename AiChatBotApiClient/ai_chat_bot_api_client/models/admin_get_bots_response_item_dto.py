import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminGetBotsResponseItemDto")


@_attrs_define
class AdminGetBotsResponseItemDto:
    """
    Attributes:
        bot_id (Union[None, Unset, str]):
        code (Union[None, Unset, str]):
        implementation_type (Union[None, Unset, str]):
        display_name (Union[None, Unset, str]):
        display_message (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        is_active (Union[Unset, bool]):
        is_start_bot (Union[Unset, bool]):
        is_fact_bot (Union[Unset, bool]):
        is_open_bot (Union[Unset, bool]):
        is_public (Union[Unset, bool]):
        is_editing_supported (Union[Unset, bool]):
        is_bot_admin (Union[Unset, bool]):
        is_bot_contributor (Union[Unset, bool]):
        created_utc (Union[Unset, datetime.datetime]):
        updated_utc (Union[Unset, datetime.datetime]):
        open_ai_service_id (Union[None, Unset, str]):
        open_ai_service (Union[None, Unset, str]):
        model_name (Union[None, Unset, str]):
    """

    bot_id: Union[None, Unset, str] = UNSET
    code: Union[None, Unset, str] = UNSET
    implementation_type: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    display_message: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_start_bot: Union[Unset, bool] = UNSET
    is_fact_bot: Union[Unset, bool] = UNSET
    is_open_bot: Union[Unset, bool] = UNSET
    is_public: Union[Unset, bool] = UNSET
    is_editing_supported: Union[Unset, bool] = UNSET
    is_bot_admin: Union[Unset, bool] = UNSET
    is_bot_contributor: Union[Unset, bool] = UNSET
    created_utc: Union[Unset, datetime.datetime] = UNSET
    updated_utc: Union[Unset, datetime.datetime] = UNSET
    open_ai_service_id: Union[None, Unset, str] = UNSET
    open_ai_service: Union[None, Unset, str] = UNSET
    model_name: Union[None, Unset, str] = UNSET

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

        implementation_type: Union[None, Unset, str]
        if isinstance(self.implementation_type, Unset):
            implementation_type = UNSET
        else:
            implementation_type = self.implementation_type

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

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_active = self.is_active

        is_start_bot = self.is_start_bot

        is_fact_bot = self.is_fact_bot

        is_open_bot = self.is_open_bot

        is_public = self.is_public

        is_editing_supported = self.is_editing_supported

        is_bot_admin = self.is_bot_admin

        is_bot_contributor = self.is_bot_contributor

        created_utc: Union[Unset, str] = UNSET
        if not isinstance(self.created_utc, Unset):
            created_utc = self.created_utc.isoformat()

        updated_utc: Union[Unset, str] = UNSET
        if not isinstance(self.updated_utc, Unset):
            updated_utc = self.updated_utc.isoformat()

        open_ai_service_id: Union[None, Unset, str]
        if isinstance(self.open_ai_service_id, Unset):
            open_ai_service_id = UNSET
        else:
            open_ai_service_id = self.open_ai_service_id

        open_ai_service: Union[None, Unset, str]
        if isinstance(self.open_ai_service, Unset):
            open_ai_service = UNSET
        else:
            open_ai_service = self.open_ai_service

        model_name: Union[None, Unset, str]
        if isinstance(self.model_name, Unset):
            model_name = UNSET
        else:
            model_name = self.model_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if code is not UNSET:
            field_dict["code"] = code
        if implementation_type is not UNSET:
            field_dict["implementationType"] = implementation_type
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_message is not UNSET:
            field_dict["displayMessage"] = display_message
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_start_bot is not UNSET:
            field_dict["isStartBot"] = is_start_bot
        if is_fact_bot is not UNSET:
            field_dict["isFactBot"] = is_fact_bot
        if is_open_bot is not UNSET:
            field_dict["isOpenBot"] = is_open_bot
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if is_editing_supported is not UNSET:
            field_dict["isEditingSupported"] = is_editing_supported
        if is_bot_admin is not UNSET:
            field_dict["isBotAdmin"] = is_bot_admin
        if is_bot_contributor is not UNSET:
            field_dict["isBotContributor"] = is_bot_contributor
        if created_utc is not UNSET:
            field_dict["createdUtc"] = created_utc
        if updated_utc is not UNSET:
            field_dict["updatedUtc"] = updated_utc
        if open_ai_service_id is not UNSET:
            field_dict["openAiServiceId"] = open_ai_service_id
        if open_ai_service is not UNSET:
            field_dict["openAiService"] = open_ai_service
        if model_name is not UNSET:
            field_dict["modelName"] = model_name

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

        def _parse_implementation_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        implementation_type = _parse_implementation_type(d.pop("implementationType", UNSET))

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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        is_active = d.pop("isActive", UNSET)

        is_start_bot = d.pop("isStartBot", UNSET)

        is_fact_bot = d.pop("isFactBot", UNSET)

        is_open_bot = d.pop("isOpenBot", UNSET)

        is_public = d.pop("isPublic", UNSET)

        is_editing_supported = d.pop("isEditingSupported", UNSET)

        is_bot_admin = d.pop("isBotAdmin", UNSET)

        is_bot_contributor = d.pop("isBotContributor", UNSET)

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

        def _parse_open_ai_service_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        open_ai_service_id = _parse_open_ai_service_id(d.pop("openAiServiceId", UNSET))

        def _parse_open_ai_service(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        open_ai_service = _parse_open_ai_service(d.pop("openAiService", UNSET))

        def _parse_model_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_name = _parse_model_name(d.pop("modelName", UNSET))

        admin_get_bots_response_item_dto = cls(
            bot_id=bot_id,
            code=code,
            implementation_type=implementation_type,
            display_name=display_name,
            display_message=display_message,
            description=description,
            is_active=is_active,
            is_start_bot=is_start_bot,
            is_fact_bot=is_fact_bot,
            is_open_bot=is_open_bot,
            is_public=is_public,
            is_editing_supported=is_editing_supported,
            is_bot_admin=is_bot_admin,
            is_bot_contributor=is_bot_contributor,
            created_utc=created_utc,
            updated_utc=updated_utc,
            open_ai_service_id=open_ai_service_id,
            open_ai_service=open_ai_service,
            model_name=model_name,
        )

        return admin_get_bots_response_item_dto

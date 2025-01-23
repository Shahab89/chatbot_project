import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.term_value_dto import TermValueDto


T = TypeVar("T", bound="AdminGetBotResponseDto")


@_attrs_define
class AdminGetBotResponseDto:
    """
    Attributes:
        bot_id (Union[None, Unset, str]):
        code (Union[None, Unset, str]):
        implementation_type (Union[None, Unset, str]):
        display_name_tv (Union[Unset, TermValueDto]):
        display_message_tv (Union[Unset, TermValueDto]):
        description_tv (Union[Unset, TermValueDto]):
        sample_question_1_tv (Union[Unset, TermValueDto]):
        sample_question_2_tv (Union[Unset, TermValueDto]):
        is_active (Union[Unset, bool]):
        is_start_bot (Union[Unset, bool]):
        base_system_message (Union[None, Unset, str]):
        is_public (Union[Unset, bool]):
        user_logins (Union[None, Unset, str]):
        user_groups (Union[None, Unset, str]):
        admin_logins (Union[None, Unset, str]):
        contributor_logins (Union[None, Unset, str]):
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
    display_name_tv: Union[Unset, "TermValueDto"] = UNSET
    display_message_tv: Union[Unset, "TermValueDto"] = UNSET
    description_tv: Union[Unset, "TermValueDto"] = UNSET
    sample_question_1_tv: Union[Unset, "TermValueDto"] = UNSET
    sample_question_2_tv: Union[Unset, "TermValueDto"] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_start_bot: Union[Unset, bool] = UNSET
    base_system_message: Union[None, Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    user_logins: Union[None, Unset, str] = UNSET
    user_groups: Union[None, Unset, str] = UNSET
    admin_logins: Union[None, Unset, str] = UNSET
    contributor_logins: Union[None, Unset, str] = UNSET
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

        display_name_tv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.display_name_tv, Unset):
            display_name_tv = self.display_name_tv.to_dict()

        display_message_tv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.display_message_tv, Unset):
            display_message_tv = self.display_message_tv.to_dict()

        description_tv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description_tv, Unset):
            description_tv = self.description_tv.to_dict()

        sample_question_1_tv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sample_question_1_tv, Unset):
            sample_question_1_tv = self.sample_question_1_tv.to_dict()

        sample_question_2_tv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sample_question_2_tv, Unset):
            sample_question_2_tv = self.sample_question_2_tv.to_dict()

        is_active = self.is_active

        is_start_bot = self.is_start_bot

        base_system_message: Union[None, Unset, str]
        if isinstance(self.base_system_message, Unset):
            base_system_message = UNSET
        else:
            base_system_message = self.base_system_message

        is_public = self.is_public

        user_logins: Union[None, Unset, str]
        if isinstance(self.user_logins, Unset):
            user_logins = UNSET
        else:
            user_logins = self.user_logins

        user_groups: Union[None, Unset, str]
        if isinstance(self.user_groups, Unset):
            user_groups = UNSET
        else:
            user_groups = self.user_groups

        admin_logins: Union[None, Unset, str]
        if isinstance(self.admin_logins, Unset):
            admin_logins = UNSET
        else:
            admin_logins = self.admin_logins

        contributor_logins: Union[None, Unset, str]
        if isinstance(self.contributor_logins, Unset):
            contributor_logins = UNSET
        else:
            contributor_logins = self.contributor_logins

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
        if display_name_tv is not UNSET:
            field_dict["displayNameTv"] = display_name_tv
        if display_message_tv is not UNSET:
            field_dict["displayMessageTv"] = display_message_tv
        if description_tv is not UNSET:
            field_dict["descriptionTv"] = description_tv
        if sample_question_1_tv is not UNSET:
            field_dict["sampleQuestion1Tv"] = sample_question_1_tv
        if sample_question_2_tv is not UNSET:
            field_dict["sampleQuestion2Tv"] = sample_question_2_tv
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_start_bot is not UNSET:
            field_dict["isStartBot"] = is_start_bot
        if base_system_message is not UNSET:
            field_dict["baseSystemMessage"] = base_system_message
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if user_logins is not UNSET:
            field_dict["userLogins"] = user_logins
        if user_groups is not UNSET:
            field_dict["userGroups"] = user_groups
        if admin_logins is not UNSET:
            field_dict["adminLogins"] = admin_logins
        if contributor_logins is not UNSET:
            field_dict["contributorLogins"] = contributor_logins
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
        from ..models.term_value_dto import TermValueDto

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

        _display_name_tv = d.pop("displayNameTv", UNSET)
        display_name_tv: Union[Unset, TermValueDto]
        if isinstance(_display_name_tv, Unset):
            display_name_tv = UNSET
        else:
            display_name_tv = TermValueDto.from_dict(_display_name_tv)

        _display_message_tv = d.pop("displayMessageTv", UNSET)
        display_message_tv: Union[Unset, TermValueDto]
        if isinstance(_display_message_tv, Unset):
            display_message_tv = UNSET
        else:
            display_message_tv = TermValueDto.from_dict(_display_message_tv)

        _description_tv = d.pop("descriptionTv", UNSET)
        description_tv: Union[Unset, TermValueDto]
        if isinstance(_description_tv, Unset):
            description_tv = UNSET
        else:
            description_tv = TermValueDto.from_dict(_description_tv)

        _sample_question_1_tv = d.pop("sampleQuestion1Tv", UNSET)
        sample_question_1_tv: Union[Unset, TermValueDto]
        if isinstance(_sample_question_1_tv, Unset):
            sample_question_1_tv = UNSET
        else:
            sample_question_1_tv = TermValueDto.from_dict(_sample_question_1_tv)

        _sample_question_2_tv = d.pop("sampleQuestion2Tv", UNSET)
        sample_question_2_tv: Union[Unset, TermValueDto]
        if isinstance(_sample_question_2_tv, Unset):
            sample_question_2_tv = UNSET
        else:
            sample_question_2_tv = TermValueDto.from_dict(_sample_question_2_tv)

        is_active = d.pop("isActive", UNSET)

        is_start_bot = d.pop("isStartBot", UNSET)

        def _parse_base_system_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        base_system_message = _parse_base_system_message(d.pop("baseSystemMessage", UNSET))

        is_public = d.pop("isPublic", UNSET)

        def _parse_user_logins(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_logins = _parse_user_logins(d.pop("userLogins", UNSET))

        def _parse_user_groups(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_groups = _parse_user_groups(d.pop("userGroups", UNSET))

        def _parse_admin_logins(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        admin_logins = _parse_admin_logins(d.pop("adminLogins", UNSET))

        def _parse_contributor_logins(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contributor_logins = _parse_contributor_logins(d.pop("contributorLogins", UNSET))

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

        admin_get_bot_response_dto = cls(
            bot_id=bot_id,
            code=code,
            implementation_type=implementation_type,
            display_name_tv=display_name_tv,
            display_message_tv=display_message_tv,
            description_tv=description_tv,
            sample_question_1_tv=sample_question_1_tv,
            sample_question_2_tv=sample_question_2_tv,
            is_active=is_active,
            is_start_bot=is_start_bot,
            base_system_message=base_system_message,
            is_public=is_public,
            user_logins=user_logins,
            user_groups=user_groups,
            admin_logins=admin_logins,
            contributor_logins=contributor_logins,
            is_bot_admin=is_bot_admin,
            is_bot_contributor=is_bot_contributor,
            created_utc=created_utc,
            updated_utc=updated_utc,
            open_ai_service_id=open_ai_service_id,
            open_ai_service=open_ai_service,
            model_name=model_name,
        )

        return admin_get_bot_response_dto

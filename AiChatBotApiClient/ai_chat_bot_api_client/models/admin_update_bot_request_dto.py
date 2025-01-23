from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.term_value_dto import TermValueDto


T = TypeVar("T", bound="AdminUpdateBotRequestDto")


@_attrs_define
class AdminUpdateBotRequestDto:
    """
    Attributes:
        code (Union[None, Unset, str]):
        display_name_tv (Union[Unset, TermValueDto]):
        display_message_tv (Union[Unset, TermValueDto]):
        description_tv (Union[Unset, TermValueDto]):
        base_system_message (Union[None, Unset, str]):
        is_active (Union[Unset, bool]):
        is_public (Union[Unset, bool]):
        user_logins (Union[None, Unset, str]):
        admin_logins (Union[None, Unset, str]):
        contributor_logins (Union[None, Unset, str]):
        sample_question_1_tv (Union[Unset, TermValueDto]):
        sample_question_2_tv (Union[Unset, TermValueDto]):
        open_ai_service_id (Union[None, Unset, str]):
        model_name (Union[None, Unset, str]):
    """

    code: Union[None, Unset, str] = UNSET
    display_name_tv: Union[Unset, "TermValueDto"] = UNSET
    display_message_tv: Union[Unset, "TermValueDto"] = UNSET
    description_tv: Union[Unset, "TermValueDto"] = UNSET
    base_system_message: Union[None, Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_public: Union[Unset, bool] = UNSET
    user_logins: Union[None, Unset, str] = UNSET
    admin_logins: Union[None, Unset, str] = UNSET
    contributor_logins: Union[None, Unset, str] = UNSET
    sample_question_1_tv: Union[Unset, "TermValueDto"] = UNSET
    sample_question_2_tv: Union[Unset, "TermValueDto"] = UNSET
    open_ai_service_id: Union[None, Unset, str] = UNSET
    model_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        display_name_tv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.display_name_tv, Unset):
            display_name_tv = self.display_name_tv.to_dict()

        display_message_tv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.display_message_tv, Unset):
            display_message_tv = self.display_message_tv.to_dict()

        description_tv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description_tv, Unset):
            description_tv = self.description_tv.to_dict()

        base_system_message: Union[None, Unset, str]
        if isinstance(self.base_system_message, Unset):
            base_system_message = UNSET
        else:
            base_system_message = self.base_system_message

        is_active = self.is_active

        is_public = self.is_public

        user_logins: Union[None, Unset, str]
        if isinstance(self.user_logins, Unset):
            user_logins = UNSET
        else:
            user_logins = self.user_logins

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

        sample_question_1_tv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sample_question_1_tv, Unset):
            sample_question_1_tv = self.sample_question_1_tv.to_dict()

        sample_question_2_tv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sample_question_2_tv, Unset):
            sample_question_2_tv = self.sample_question_2_tv.to_dict()

        open_ai_service_id: Union[None, Unset, str]
        if isinstance(self.open_ai_service_id, Unset):
            open_ai_service_id = UNSET
        else:
            open_ai_service_id = self.open_ai_service_id

        model_name: Union[None, Unset, str]
        if isinstance(self.model_name, Unset):
            model_name = UNSET
        else:
            model_name = self.model_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if display_name_tv is not UNSET:
            field_dict["displayNameTv"] = display_name_tv
        if display_message_tv is not UNSET:
            field_dict["displayMessageTv"] = display_message_tv
        if description_tv is not UNSET:
            field_dict["descriptionTv"] = description_tv
        if base_system_message is not UNSET:
            field_dict["baseSystemMessage"] = base_system_message
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if user_logins is not UNSET:
            field_dict["userLogins"] = user_logins
        if admin_logins is not UNSET:
            field_dict["adminLogins"] = admin_logins
        if contributor_logins is not UNSET:
            field_dict["contributorLogins"] = contributor_logins
        if sample_question_1_tv is not UNSET:
            field_dict["sampleQuestion1Tv"] = sample_question_1_tv
        if sample_question_2_tv is not UNSET:
            field_dict["sampleQuestion2Tv"] = sample_question_2_tv
        if open_ai_service_id is not UNSET:
            field_dict["openAiServiceId"] = open_ai_service_id
        if model_name is not UNSET:
            field_dict["modelName"] = model_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.term_value_dto import TermValueDto

        d = src_dict.copy()

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

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

        def _parse_base_system_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        base_system_message = _parse_base_system_message(d.pop("baseSystemMessage", UNSET))

        is_active = d.pop("isActive", UNSET)

        is_public = d.pop("isPublic", UNSET)

        def _parse_user_logins(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_logins = _parse_user_logins(d.pop("userLogins", UNSET))

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

        def _parse_open_ai_service_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        open_ai_service_id = _parse_open_ai_service_id(d.pop("openAiServiceId", UNSET))

        def _parse_model_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_name = _parse_model_name(d.pop("modelName", UNSET))

        admin_update_bot_request_dto = cls(
            code=code,
            display_name_tv=display_name_tv,
            display_message_tv=display_message_tv,
            description_tv=description_tv,
            base_system_message=base_system_message,
            is_active=is_active,
            is_public=is_public,
            user_logins=user_logins,
            admin_logins=admin_logins,
            contributor_logins=contributor_logins,
            sample_question_1_tv=sample_question_1_tv,
            sample_question_2_tv=sample_question_2_tv,
            open_ai_service_id=open_ai_service_id,
            model_name=model_name,
        )

        return admin_update_bot_request_dto

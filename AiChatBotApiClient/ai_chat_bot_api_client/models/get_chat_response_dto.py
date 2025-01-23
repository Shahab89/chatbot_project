import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_chat_response_completion_dto import GetChatResponseCompletionDto


T = TypeVar("T", bound="GetChatResponseDto")


@_attrs_define
class GetChatResponseDto:
    """
    Attributes:
        chat_id (Union[None, Unset, str]):
        display_name (Union[None, Unset, str]):
        created_utc (Union[Unset, datetime.datetime]):
        last_accessed_utc (Union[Unset, datetime.datetime]):
        bot_id (Union[None, Unset, str]):
        bot_display_name (Union[None, Unset, str]):
        bot_display_message (Union[None, Unset, str]):
        bot_description (Union[None, Unset, str]):
        bot_sample_question_1 (Union[None, Unset, str]):
        bot_sample_question_2 (Union[None, Unset, str]):
        completions (Union[List['GetChatResponseCompletionDto'], None, Unset]):
        is_favorite (Union[Unset, bool]):
        is_user_system_message_supported (Union[Unset, bool]):
        user_system_message_id (Union[None, Unset, str]):
        user_system_message_display_name (Union[None, Unset, str]):
    """

    chat_id: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    created_utc: Union[Unset, datetime.datetime] = UNSET
    last_accessed_utc: Union[Unset, datetime.datetime] = UNSET
    bot_id: Union[None, Unset, str] = UNSET
    bot_display_name: Union[None, Unset, str] = UNSET
    bot_display_message: Union[None, Unset, str] = UNSET
    bot_description: Union[None, Unset, str] = UNSET
    bot_sample_question_1: Union[None, Unset, str] = UNSET
    bot_sample_question_2: Union[None, Unset, str] = UNSET
    completions: Union[List["GetChatResponseCompletionDto"], None, Unset] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    is_user_system_message_supported: Union[Unset, bool] = UNSET
    user_system_message_id: Union[None, Unset, str] = UNSET
    user_system_message_display_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        chat_id: Union[None, Unset, str]
        if isinstance(self.chat_id, Unset):
            chat_id = UNSET
        else:
            chat_id = self.chat_id

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        created_utc: Union[Unset, str] = UNSET
        if not isinstance(self.created_utc, Unset):
            created_utc = self.created_utc.isoformat()

        last_accessed_utc: Union[Unset, str] = UNSET
        if not isinstance(self.last_accessed_utc, Unset):
            last_accessed_utc = self.last_accessed_utc.isoformat()

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

        bot_sample_question_1: Union[None, Unset, str]
        if isinstance(self.bot_sample_question_1, Unset):
            bot_sample_question_1 = UNSET
        else:
            bot_sample_question_1 = self.bot_sample_question_1

        bot_sample_question_2: Union[None, Unset, str]
        if isinstance(self.bot_sample_question_2, Unset):
            bot_sample_question_2 = UNSET
        else:
            bot_sample_question_2 = self.bot_sample_question_2

        completions: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.completions, Unset):
            completions = UNSET
        elif isinstance(self.completions, list):
            completions = []
            for completions_type_0_item_data in self.completions:
                completions_type_0_item = completions_type_0_item_data.to_dict()
                completions.append(completions_type_0_item)

        else:
            completions = self.completions

        is_favorite = self.is_favorite

        is_user_system_message_supported = self.is_user_system_message_supported

        user_system_message_id: Union[None, Unset, str]
        if isinstance(self.user_system_message_id, Unset):
            user_system_message_id = UNSET
        else:
            user_system_message_id = self.user_system_message_id

        user_system_message_display_name: Union[None, Unset, str]
        if isinstance(self.user_system_message_display_name, Unset):
            user_system_message_display_name = UNSET
        else:
            user_system_message_display_name = self.user_system_message_display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if created_utc is not UNSET:
            field_dict["createdUtc"] = created_utc
        if last_accessed_utc is not UNSET:
            field_dict["lastAccessedUtc"] = last_accessed_utc
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if bot_display_name is not UNSET:
            field_dict["botDisplayName"] = bot_display_name
        if bot_display_message is not UNSET:
            field_dict["botDisplayMessage"] = bot_display_message
        if bot_description is not UNSET:
            field_dict["botDescription"] = bot_description
        if bot_sample_question_1 is not UNSET:
            field_dict["botSampleQuestion1"] = bot_sample_question_1
        if bot_sample_question_2 is not UNSET:
            field_dict["botSampleQuestion2"] = bot_sample_question_2
        if completions is not UNSET:
            field_dict["completions"] = completions
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if is_user_system_message_supported is not UNSET:
            field_dict["isUserSystemMessageSupported"] = is_user_system_message_supported
        if user_system_message_id is not UNSET:
            field_dict["userSystemMessageId"] = user_system_message_id
        if user_system_message_display_name is not UNSET:
            field_dict["userSystemMessageDisplayName"] = user_system_message_display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_chat_response_completion_dto import GetChatResponseCompletionDto

        d = src_dict.copy()

        def _parse_chat_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chat_id = _parse_chat_id(d.pop("chatId", UNSET))

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        _created_utc = d.pop("createdUtc", UNSET)
        created_utc: Union[Unset, datetime.datetime]
        if isinstance(_created_utc, Unset):
            created_utc = UNSET
        else:
            created_utc = isoparse(_created_utc)

        _last_accessed_utc = d.pop("lastAccessedUtc", UNSET)
        last_accessed_utc: Union[Unset, datetime.datetime]
        if isinstance(_last_accessed_utc, Unset):
            last_accessed_utc = UNSET
        else:
            last_accessed_utc = isoparse(_last_accessed_utc)

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

        def _parse_bot_sample_question_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_sample_question_1 = _parse_bot_sample_question_1(d.pop("botSampleQuestion1", UNSET))

        def _parse_bot_sample_question_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_sample_question_2 = _parse_bot_sample_question_2(d.pop("botSampleQuestion2", UNSET))

        def _parse_completions(data: object) -> Union[List["GetChatResponseCompletionDto"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                completions_type_0 = []
                _completions_type_0 = data
                for completions_type_0_item_data in _completions_type_0:
                    completions_type_0_item = GetChatResponseCompletionDto.from_dict(completions_type_0_item_data)

                    completions_type_0.append(completions_type_0_item)

                return completions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["GetChatResponseCompletionDto"], None, Unset], data)

        completions = _parse_completions(d.pop("completions", UNSET))

        is_favorite = d.pop("isFavorite", UNSET)

        is_user_system_message_supported = d.pop("isUserSystemMessageSupported", UNSET)

        def _parse_user_system_message_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_system_message_id = _parse_user_system_message_id(d.pop("userSystemMessageId", UNSET))

        def _parse_user_system_message_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_system_message_display_name = _parse_user_system_message_display_name(
            d.pop("userSystemMessageDisplayName", UNSET)
        )

        get_chat_response_dto = cls(
            chat_id=chat_id,
            display_name=display_name,
            created_utc=created_utc,
            last_accessed_utc=last_accessed_utc,
            bot_id=bot_id,
            bot_display_name=bot_display_name,
            bot_display_message=bot_display_message,
            bot_description=bot_description,
            bot_sample_question_1=bot_sample_question_1,
            bot_sample_question_2=bot_sample_question_2,
            completions=completions,
            is_favorite=is_favorite,
            is_user_system_message_supported=is_user_system_message_supported,
            user_system_message_id=user_system_message_id,
            user_system_message_display_name=user_system_message_display_name,
        )

        return get_chat_response_dto

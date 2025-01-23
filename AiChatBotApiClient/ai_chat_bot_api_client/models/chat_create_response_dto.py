from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCreateResponseDto")


@_attrs_define
class ChatCreateResponseDto:
    """
    Attributes:
        chat_id (Union[None, Unset, str]):
        bot_id (Union[None, Unset, str]):
        bot_display_name (Union[None, Unset, str]):
        bot_display_message (Union[None, Unset, str]):
        bot_description (Union[None, Unset, str]):
        bot_sample_question_1 (Union[None, Unset, str]):
        bot_sample_question_2 (Union[None, Unset, str]):
        is_user_system_message_supported (Union[Unset, bool]):
    """

    chat_id: Union[None, Unset, str] = UNSET
    bot_id: Union[None, Unset, str] = UNSET
    bot_display_name: Union[None, Unset, str] = UNSET
    bot_display_message: Union[None, Unset, str] = UNSET
    bot_description: Union[None, Unset, str] = UNSET
    bot_sample_question_1: Union[None, Unset, str] = UNSET
    bot_sample_question_2: Union[None, Unset, str] = UNSET
    is_user_system_message_supported: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        chat_id: Union[None, Unset, str]
        if isinstance(self.chat_id, Unset):
            chat_id = UNSET
        else:
            chat_id = self.chat_id

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

        is_user_system_message_supported = self.is_user_system_message_supported

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
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
        if is_user_system_message_supported is not UNSET:
            field_dict["isUserSystemMessageSupported"] = is_user_system_message_supported

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_chat_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chat_id = _parse_chat_id(d.pop("chatId", UNSET))

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

        is_user_system_message_supported = d.pop("isUserSystemMessageSupported", UNSET)

        chat_create_response_dto = cls(
            chat_id=chat_id,
            bot_id=bot_id,
            bot_display_name=bot_display_name,
            bot_display_message=bot_display_message,
            bot_description=bot_description,
            bot_sample_question_1=bot_sample_question_1,
            bot_sample_question_2=bot_sample_question_2,
            is_user_system_message_supported=is_user_system_message_supported,
        )

        return chat_create_response_dto

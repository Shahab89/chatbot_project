import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotFeedbackRequestDto")


@_attrs_define
class BotFeedbackRequestDto:
    """
    Attributes:
        chat_id (Union[None, Unset, str]):
        user_message (Union[None, Unset, str]):
        assistant_message (Union[None, Unset, str]):
        message_created_utc (Union[Unset, datetime.datetime]):
        user_comment (Union[None, Unset, str]):
        vote_id (Union[Unset, int]):
    """

    chat_id: Union[None, Unset, str] = UNSET
    user_message: Union[None, Unset, str] = UNSET
    assistant_message: Union[None, Unset, str] = UNSET
    message_created_utc: Union[Unset, datetime.datetime] = UNSET
    user_comment: Union[None, Unset, str] = UNSET
    vote_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        chat_id: Union[None, Unset, str]
        if isinstance(self.chat_id, Unset):
            chat_id = UNSET
        else:
            chat_id = self.chat_id

        user_message: Union[None, Unset, str]
        if isinstance(self.user_message, Unset):
            user_message = UNSET
        else:
            user_message = self.user_message

        assistant_message: Union[None, Unset, str]
        if isinstance(self.assistant_message, Unset):
            assistant_message = UNSET
        else:
            assistant_message = self.assistant_message

        message_created_utc: Union[Unset, str] = UNSET
        if not isinstance(self.message_created_utc, Unset):
            message_created_utc = self.message_created_utc.isoformat()

        user_comment: Union[None, Unset, str]
        if isinstance(self.user_comment, Unset):
            user_comment = UNSET
        else:
            user_comment = self.user_comment

        vote_id = self.vote_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if user_message is not UNSET:
            field_dict["userMessage"] = user_message
        if assistant_message is not UNSET:
            field_dict["assistantMessage"] = assistant_message
        if message_created_utc is not UNSET:
            field_dict["messageCreatedUtc"] = message_created_utc
        if user_comment is not UNSET:
            field_dict["userComment"] = user_comment
        if vote_id is not UNSET:
            field_dict["voteId"] = vote_id

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

        def _parse_user_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_message = _parse_user_message(d.pop("userMessage", UNSET))

        def _parse_assistant_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assistant_message = _parse_assistant_message(d.pop("assistantMessage", UNSET))

        _message_created_utc = d.pop("messageCreatedUtc", UNSET)
        message_created_utc: Union[Unset, datetime.datetime]
        if isinstance(_message_created_utc, Unset):
            message_created_utc = UNSET
        else:
            message_created_utc = isoparse(_message_created_utc)

        def _parse_user_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_comment = _parse_user_comment(d.pop("userComment", UNSET))

        vote_id = d.pop("voteId", UNSET)

        bot_feedback_request_dto = cls(
            chat_id=chat_id,
            user_message=user_message,
            assistant_message=assistant_message,
            message_created_utc=message_created_utc,
            user_comment=user_comment,
            vote_id=vote_id,
        )

        return bot_feedback_request_dto

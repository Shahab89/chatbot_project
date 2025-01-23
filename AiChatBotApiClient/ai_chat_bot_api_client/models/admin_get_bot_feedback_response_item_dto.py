import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminGetBotFeedbackResponseItemDto")


@_attrs_define
class AdminGetBotFeedbackResponseItemDto:
    """
    Attributes:
        id (Union[None, Unset, str]):
        bot_id (Union[None, Unset, str]):
        user_message (Union[None, Unset, str]):
        assistant_message (Union[None, Unset, str]):
        user_comment (Union[None, Unset, str]):
        message_created_utc (Union[Unset, datetime.datetime]):
        created_utc (Union[Unset, datetime.datetime]):
        vote_id (Union[Unset, int]):
        status (Union[None, Unset, int]):
        admin_comment (Union[None, Unset, str]):
        admin_updated_utc (Union[None, Unset, datetime.datetime]):
    """

    id: Union[None, Unset, str] = UNSET
    bot_id: Union[None, Unset, str] = UNSET
    user_message: Union[None, Unset, str] = UNSET
    assistant_message: Union[None, Unset, str] = UNSET
    user_comment: Union[None, Unset, str] = UNSET
    message_created_utc: Union[Unset, datetime.datetime] = UNSET
    created_utc: Union[Unset, datetime.datetime] = UNSET
    vote_id: Union[Unset, int] = UNSET
    status: Union[None, Unset, int] = UNSET
    admin_comment: Union[None, Unset, str] = UNSET
    admin_updated_utc: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        bot_id: Union[None, Unset, str]
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

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

        user_comment: Union[None, Unset, str]
        if isinstance(self.user_comment, Unset):
            user_comment = UNSET
        else:
            user_comment = self.user_comment

        message_created_utc: Union[Unset, str] = UNSET
        if not isinstance(self.message_created_utc, Unset):
            message_created_utc = self.message_created_utc.isoformat()

        created_utc: Union[Unset, str] = UNSET
        if not isinstance(self.created_utc, Unset):
            created_utc = self.created_utc.isoformat()

        vote_id = self.vote_id

        status: Union[None, Unset, int]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        admin_comment: Union[None, Unset, str]
        if isinstance(self.admin_comment, Unset):
            admin_comment = UNSET
        else:
            admin_comment = self.admin_comment

        admin_updated_utc: Union[None, Unset, str]
        if isinstance(self.admin_updated_utc, Unset):
            admin_updated_utc = UNSET
        elif isinstance(self.admin_updated_utc, datetime.datetime):
            admin_updated_utc = self.admin_updated_utc.isoformat()
        else:
            admin_updated_utc = self.admin_updated_utc

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if user_message is not UNSET:
            field_dict["userMessage"] = user_message
        if assistant_message is not UNSET:
            field_dict["assistantMessage"] = assistant_message
        if user_comment is not UNSET:
            field_dict["userComment"] = user_comment
        if message_created_utc is not UNSET:
            field_dict["messageCreatedUtc"] = message_created_utc
        if created_utc is not UNSET:
            field_dict["createdUtc"] = created_utc
        if vote_id is not UNSET:
            field_dict["voteId"] = vote_id
        if status is not UNSET:
            field_dict["status"] = status
        if admin_comment is not UNSET:
            field_dict["adminComment"] = admin_comment
        if admin_updated_utc is not UNSET:
            field_dict["adminUpdatedUtc"] = admin_updated_utc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_bot_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bot_id = _parse_bot_id(d.pop("botId", UNSET))

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

        def _parse_user_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_comment = _parse_user_comment(d.pop("userComment", UNSET))

        _message_created_utc = d.pop("messageCreatedUtc", UNSET)
        message_created_utc: Union[Unset, datetime.datetime]
        if isinstance(_message_created_utc, Unset):
            message_created_utc = UNSET
        else:
            message_created_utc = isoparse(_message_created_utc)

        _created_utc = d.pop("createdUtc", UNSET)
        created_utc: Union[Unset, datetime.datetime]
        if isinstance(_created_utc, Unset):
            created_utc = UNSET
        else:
            created_utc = isoparse(_created_utc)

        vote_id = d.pop("voteId", UNSET)

        def _parse_status(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_admin_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        admin_comment = _parse_admin_comment(d.pop("adminComment", UNSET))

        def _parse_admin_updated_utc(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                admin_updated_utc_type_0 = isoparse(data)

                return admin_updated_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        admin_updated_utc = _parse_admin_updated_utc(d.pop("adminUpdatedUtc", UNSET))

        admin_get_bot_feedback_response_item_dto = cls(
            id=id,
            bot_id=bot_id,
            user_message=user_message,
            assistant_message=assistant_message,
            user_comment=user_comment,
            message_created_utc=message_created_utc,
            created_utc=created_utc,
            vote_id=vote_id,
            status=status,
            admin_comment=admin_comment,
            admin_updated_utc=admin_updated_utc,
        )

        return admin_get_bot_feedback_response_item_dto

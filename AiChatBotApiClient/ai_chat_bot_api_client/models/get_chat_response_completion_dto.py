import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_meta_data import ChatCompletionMetaData


T = TypeVar("T", bound="GetChatResponseCompletionDto")


@_attrs_define
class GetChatResponseCompletionDto:
    """
    Attributes:
        completion_id (Union[None, Unset, str]):
        user_message (Union[None, Unset, str]):
        assistant_message (Union[None, Unset, str]):
        created_utc (Union[Unset, datetime.datetime]):
        meta_data (Union[Unset, ChatCompletionMetaData]):
    """

    completion_id: Union[None, Unset, str] = UNSET
    user_message: Union[None, Unset, str] = UNSET
    assistant_message: Union[None, Unset, str] = UNSET
    created_utc: Union[Unset, datetime.datetime] = UNSET
    meta_data: Union[Unset, "ChatCompletionMetaData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        completion_id: Union[None, Unset, str]
        if isinstance(self.completion_id, Unset):
            completion_id = UNSET
        else:
            completion_id = self.completion_id

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

        created_utc: Union[Unset, str] = UNSET
        if not isinstance(self.created_utc, Unset):
            created_utc = self.created_utc.isoformat()

        meta_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if completion_id is not UNSET:
            field_dict["completionId"] = completion_id
        if user_message is not UNSET:
            field_dict["userMessage"] = user_message
        if assistant_message is not UNSET:
            field_dict["assistantMessage"] = assistant_message
        if created_utc is not UNSET:
            field_dict["createdUtc"] = created_utc
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_completion_meta_data import ChatCompletionMetaData

        d = src_dict.copy()

        def _parse_completion_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        completion_id = _parse_completion_id(d.pop("completionId", UNSET))

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

        _created_utc = d.pop("createdUtc", UNSET)
        created_utc: Union[Unset, datetime.datetime]
        if isinstance(_created_utc, Unset):
            created_utc = UNSET
        else:
            created_utc = isoparse(_created_utc)

        _meta_data = d.pop("metaData", UNSET)
        meta_data: Union[Unset, ChatCompletionMetaData]
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = ChatCompletionMetaData.from_dict(_meta_data)

        get_chat_response_completion_dto = cls(
            completion_id=completion_id,
            user_message=user_message,
            assistant_message=assistant_message,
            created_utc=created_utc,
            meta_data=meta_data,
        )

        return get_chat_response_completion_dto

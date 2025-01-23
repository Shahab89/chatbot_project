from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCompletionRequestDto")


@_attrs_define
class ChatCompletionRequestDto:
    """
    Attributes:
        user_message (Union[None, Unset, str]):
        ignore_chat_history (Union[Unset, bool]):
        is_admin_chat (Union[Unset, bool]):
        is_trace_log_enabled (Union[Unset, bool]):
    """

    user_message: Union[None, Unset, str] = UNSET
    ignore_chat_history: Union[Unset, bool] = UNSET
    is_admin_chat: Union[Unset, bool] = UNSET
    is_trace_log_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_message: Union[None, Unset, str]
        if isinstance(self.user_message, Unset):
            user_message = UNSET
        else:
            user_message = self.user_message

        ignore_chat_history = self.ignore_chat_history

        is_admin_chat = self.is_admin_chat

        is_trace_log_enabled = self.is_trace_log_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_message is not UNSET:
            field_dict["userMessage"] = user_message
        if ignore_chat_history is not UNSET:
            field_dict["ignoreChatHistory"] = ignore_chat_history
        if is_admin_chat is not UNSET:
            field_dict["isAdminChat"] = is_admin_chat
        if is_trace_log_enabled is not UNSET:
            field_dict["isTraceLogEnabled"] = is_trace_log_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_user_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_message = _parse_user_message(d.pop("userMessage", UNSET))

        ignore_chat_history = d.pop("ignoreChatHistory", UNSET)

        is_admin_chat = d.pop("isAdminChat", UNSET)

        is_trace_log_enabled = d.pop("isTraceLogEnabled", UNSET)

        chat_completion_request_dto = cls(
            user_message=user_message,
            ignore_chat_history=ignore_chat_history,
            is_admin_chat=is_admin_chat,
            is_trace_log_enabled=is_trace_log_enabled,
        )

        return chat_completion_request_dto

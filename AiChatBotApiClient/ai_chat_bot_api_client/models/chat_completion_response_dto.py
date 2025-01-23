from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_meta_data import ChatCompletionMetaData


T = TypeVar("T", bound="ChatCompletionResponseDto")


@_attrs_define
class ChatCompletionResponseDto:
    """
    Attributes:
        completion_id (Union[None, Unset, str]):
        chat_id (Union[None, Unset, str]):
        user_message (Union[None, Unset, str]):
        assistant_message (Union[None, Unset, str]):
        prompt_tokens (Union[Unset, int]):
        completion_tokens (Union[Unset, int]):
        total_tokens (Union[Unset, int]):
        bot_id (Union[None, Unset, str]):
        bot_display_name (Union[None, Unset, str]):
        bot_display_message (Union[None, Unset, str]):
        bot_description (Union[None, Unset, str]):
        chat_display_name (Union[None, Unset, str]):
        meta_data (Union[Unset, ChatCompletionMetaData]):
        trace_log (Union[None, Unset, str]):
    """

    completion_id: Union[None, Unset, str] = UNSET
    chat_id: Union[None, Unset, str] = UNSET
    user_message: Union[None, Unset, str] = UNSET
    assistant_message: Union[None, Unset, str] = UNSET
    prompt_tokens: Union[Unset, int] = UNSET
    completion_tokens: Union[Unset, int] = UNSET
    total_tokens: Union[Unset, int] = UNSET
    bot_id: Union[None, Unset, str] = UNSET
    bot_display_name: Union[None, Unset, str] = UNSET
    bot_display_message: Union[None, Unset, str] = UNSET
    bot_description: Union[None, Unset, str] = UNSET
    chat_display_name: Union[None, Unset, str] = UNSET
    meta_data: Union[Unset, "ChatCompletionMetaData"] = UNSET
    trace_log: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        completion_id: Union[None, Unset, str]
        if isinstance(self.completion_id, Unset):
            completion_id = UNSET
        else:
            completion_id = self.completion_id

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

        prompt_tokens = self.prompt_tokens

        completion_tokens = self.completion_tokens

        total_tokens = self.total_tokens

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

        chat_display_name: Union[None, Unset, str]
        if isinstance(self.chat_display_name, Unset):
            chat_display_name = UNSET
        else:
            chat_display_name = self.chat_display_name

        meta_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        trace_log: Union[None, Unset, str]
        if isinstance(self.trace_log, Unset):
            trace_log = UNSET
        else:
            trace_log = self.trace_log

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if completion_id is not UNSET:
            field_dict["completionId"] = completion_id
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if user_message is not UNSET:
            field_dict["userMessage"] = user_message
        if assistant_message is not UNSET:
            field_dict["assistantMessage"] = assistant_message
        if prompt_tokens is not UNSET:
            field_dict["promptTokens"] = prompt_tokens
        if completion_tokens is not UNSET:
            field_dict["completionTokens"] = completion_tokens
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if bot_display_name is not UNSET:
            field_dict["botDisplayName"] = bot_display_name
        if bot_display_message is not UNSET:
            field_dict["botDisplayMessage"] = bot_display_message
        if bot_description is not UNSET:
            field_dict["botDescription"] = bot_description
        if chat_display_name is not UNSET:
            field_dict["chatDisplayName"] = chat_display_name
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if trace_log is not UNSET:
            field_dict["traceLog"] = trace_log

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

        prompt_tokens = d.pop("promptTokens", UNSET)

        completion_tokens = d.pop("completionTokens", UNSET)

        total_tokens = d.pop("totalTokens", UNSET)

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

        def _parse_chat_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chat_display_name = _parse_chat_display_name(d.pop("chatDisplayName", UNSET))

        _meta_data = d.pop("metaData", UNSET)
        meta_data: Union[Unset, ChatCompletionMetaData]
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = ChatCompletionMetaData.from_dict(_meta_data)

        def _parse_trace_log(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        trace_log = _parse_trace_log(d.pop("traceLog", UNSET))

        chat_completion_response_dto = cls(
            completion_id=completion_id,
            chat_id=chat_id,
            user_message=user_message,
            assistant_message=assistant_message,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=total_tokens,
            bot_id=bot_id,
            bot_display_name=bot_display_name,
            bot_display_message=bot_display_message,
            bot_description=bot_description,
            chat_display_name=chat_display_name,
            meta_data=meta_data,
            trace_log=trace_log,
        )

        return chat_completion_response_dto

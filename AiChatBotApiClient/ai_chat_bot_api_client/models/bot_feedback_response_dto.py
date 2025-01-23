from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotFeedbackResponseDto")


@_attrs_define
class BotFeedbackResponseDto:
    """
    Attributes:
        feedback_id (Union[None, Unset, str]):
    """

    feedback_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        feedback_id: Union[None, Unset, str]
        if isinstance(self.feedback_id, Unset):
            feedback_id = UNSET
        else:
            feedback_id = self.feedback_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if feedback_id is not UNSET:
            field_dict["feedbackId"] = feedback_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_feedback_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        feedback_id = _parse_feedback_id(d.pop("feedbackId", UNSET))

        bot_feedback_response_dto = cls(
            feedback_id=feedback_id,
        )

        return bot_feedback_response_dto

from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminUpdateBotFeedbackRequestDto")


@_attrs_define
class AdminUpdateBotFeedbackRequestDto:
    """
    Attributes:
        status (Union[Unset, int]):
        admin_comment (Union[None, Unset, str]):
    """

    status: Union[Unset, int] = UNSET
    admin_comment: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        admin_comment: Union[None, Unset, str]
        if isinstance(self.admin_comment, Unset):
            admin_comment = UNSET
        else:
            admin_comment = self.admin_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if admin_comment is not UNSET:
            field_dict["adminComment"] = admin_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        def _parse_admin_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        admin_comment = _parse_admin_comment(d.pop("adminComment", UNSET))

        admin_update_bot_feedback_request_dto = cls(
            status=status,
            admin_comment=admin_comment,
        )

        return admin_update_bot_feedback_request_dto

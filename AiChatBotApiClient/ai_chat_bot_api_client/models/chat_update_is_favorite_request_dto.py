from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatUpdateIsFavoriteRequestDto")


@_attrs_define
class ChatUpdateIsFavoriteRequestDto:
    """
    Attributes:
        is_favorite (Union[Unset, bool]):
    """

    is_favorite: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_favorite = self.is_favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_favorite = d.pop("isFavorite", UNSET)

        chat_update_is_favorite_request_dto = cls(
            is_favorite=is_favorite,
        )

        return chat_update_is_favorite_request_dto

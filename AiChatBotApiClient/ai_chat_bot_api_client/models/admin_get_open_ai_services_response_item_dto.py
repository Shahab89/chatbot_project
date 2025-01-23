from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminGetOpenAiServicesResponseItemDto")


@_attrs_define
class AdminGetOpenAiServicesResponseItemDto:
    """
    Attributes:
        id (Union[None, Unset, str]):
        display_name (Union[None, Unset, str]):
        is_active (Union[Unset, bool]):
    """

    id: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

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

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        is_active = d.pop("isActive", UNSET)

        admin_get_open_ai_services_response_item_dto = cls(
            id=id,
            display_name=display_name,
            is_active=is_active,
        )

        return admin_get_open_ai_services_response_item_dto

from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminGetOpenAiServiceResponseDto")


@_attrs_define
class AdminGetOpenAiServiceResponseDto:
    """
    Attributes:
        display_name (Union[None, Unset, str]):
        is_active (Union[Unset, bool]):
        is_azure_open_ai_set (Union[Unset, bool]):
        azure_open_ai_endpoint (Union[None, Unset, str]):
    """

    display_name: Union[None, Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_azure_open_ai_set: Union[Unset, bool] = UNSET
    azure_open_ai_endpoint: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        is_active = self.is_active

        is_azure_open_ai_set = self.is_azure_open_ai_set

        azure_open_ai_endpoint: Union[None, Unset, str]
        if isinstance(self.azure_open_ai_endpoint, Unset):
            azure_open_ai_endpoint = UNSET
        else:
            azure_open_ai_endpoint = self.azure_open_ai_endpoint

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_azure_open_ai_set is not UNSET:
            field_dict["isAzureOpenAiSet"] = is_azure_open_ai_set
        if azure_open_ai_endpoint is not UNSET:
            field_dict["azureOpenAiEndpoint"] = azure_open_ai_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        is_active = d.pop("isActive", UNSET)

        is_azure_open_ai_set = d.pop("isAzureOpenAiSet", UNSET)

        def _parse_azure_open_ai_endpoint(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        azure_open_ai_endpoint = _parse_azure_open_ai_endpoint(d.pop("azureOpenAiEndpoint", UNSET))

        admin_get_open_ai_service_response_dto = cls(
            display_name=display_name,
            is_active=is_active,
            is_azure_open_ai_set=is_azure_open_ai_set,
            azure_open_ai_endpoint=azure_open_ai_endpoint,
        )

        return admin_get_open_ai_service_response_dto

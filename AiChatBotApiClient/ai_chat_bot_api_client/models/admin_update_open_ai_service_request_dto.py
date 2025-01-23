from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminUpdateOpenAiServiceRequestDto")


@_attrs_define
class AdminUpdateOpenAiServiceRequestDto:
    """
    Attributes:
        display_name (Union[None, Unset, str]):
        is_active (Union[Unset, bool]):
        is_update_open_ai (Union[Unset, bool]):
        azure_open_ai_endpoint (Union[None, Unset, str]):
        azure_open_ai_api_key (Union[None, Unset, str]):
    """

    display_name: Union[None, Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_update_open_ai: Union[Unset, bool] = UNSET
    azure_open_ai_endpoint: Union[None, Unset, str] = UNSET
    azure_open_ai_api_key: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        is_active = self.is_active

        is_update_open_ai = self.is_update_open_ai

        azure_open_ai_endpoint: Union[None, Unset, str]
        if isinstance(self.azure_open_ai_endpoint, Unset):
            azure_open_ai_endpoint = UNSET
        else:
            azure_open_ai_endpoint = self.azure_open_ai_endpoint

        azure_open_ai_api_key: Union[None, Unset, str]
        if isinstance(self.azure_open_ai_api_key, Unset):
            azure_open_ai_api_key = UNSET
        else:
            azure_open_ai_api_key = self.azure_open_ai_api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_update_open_ai is not UNSET:
            field_dict["isUpdateOpenAi"] = is_update_open_ai
        if azure_open_ai_endpoint is not UNSET:
            field_dict["azureOpenAiEndpoint"] = azure_open_ai_endpoint
        if azure_open_ai_api_key is not UNSET:
            field_dict["azureOpenAiApiKey"] = azure_open_ai_api_key

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

        is_update_open_ai = d.pop("isUpdateOpenAi", UNSET)

        def _parse_azure_open_ai_endpoint(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        azure_open_ai_endpoint = _parse_azure_open_ai_endpoint(d.pop("azureOpenAiEndpoint", UNSET))

        def _parse_azure_open_ai_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        azure_open_ai_api_key = _parse_azure_open_ai_api_key(d.pop("azureOpenAiApiKey", UNSET))

        admin_update_open_ai_service_request_dto = cls(
            display_name=display_name,
            is_active=is_active,
            is_update_open_ai=is_update_open_ai,
            azure_open_ai_endpoint=azure_open_ai_endpoint,
            azure_open_ai_api_key=azure_open_ai_api_key,
        )

        return admin_update_open_ai_service_request_dto

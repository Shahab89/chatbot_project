from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminGetAcsBotConfigurationResponseDto")


@_attrs_define
class AdminGetAcsBotConfigurationResponseDto:
    """
    Attributes:
        is_blob_service_client_set (Union[Unset, bool]):
        blob_service_client_display_uri (Union[None, Unset, str]):
        is_search_client_set (Union[Unset, bool]):
        search_client_endpoint (Union[None, Unset, str]):
        index_name (Union[None, Unset, str]):
        index_fields (Union[None, Unset, str]):
        use_semantic_search (Union[Unset, bool]):
        semantic_search_configuration_name (Union[None, Unset, str]):
        max_results (Union[None, Unset, int]):
        max_chars_total (Union[None, Unset, int]):
    """

    is_blob_service_client_set: Union[Unset, bool] = UNSET
    blob_service_client_display_uri: Union[None, Unset, str] = UNSET
    is_search_client_set: Union[Unset, bool] = UNSET
    search_client_endpoint: Union[None, Unset, str] = UNSET
    index_name: Union[None, Unset, str] = UNSET
    index_fields: Union[None, Unset, str] = UNSET
    use_semantic_search: Union[Unset, bool] = UNSET
    semantic_search_configuration_name: Union[None, Unset, str] = UNSET
    max_results: Union[None, Unset, int] = UNSET
    max_chars_total: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_blob_service_client_set = self.is_blob_service_client_set

        blob_service_client_display_uri: Union[None, Unset, str]
        if isinstance(self.blob_service_client_display_uri, Unset):
            blob_service_client_display_uri = UNSET
        else:
            blob_service_client_display_uri = self.blob_service_client_display_uri

        is_search_client_set = self.is_search_client_set

        search_client_endpoint: Union[None, Unset, str]
        if isinstance(self.search_client_endpoint, Unset):
            search_client_endpoint = UNSET
        else:
            search_client_endpoint = self.search_client_endpoint

        index_name: Union[None, Unset, str]
        if isinstance(self.index_name, Unset):
            index_name = UNSET
        else:
            index_name = self.index_name

        index_fields: Union[None, Unset, str]
        if isinstance(self.index_fields, Unset):
            index_fields = UNSET
        else:
            index_fields = self.index_fields

        use_semantic_search = self.use_semantic_search

        semantic_search_configuration_name: Union[None, Unset, str]
        if isinstance(self.semantic_search_configuration_name, Unset):
            semantic_search_configuration_name = UNSET
        else:
            semantic_search_configuration_name = self.semantic_search_configuration_name

        max_results: Union[None, Unset, int]
        if isinstance(self.max_results, Unset):
            max_results = UNSET
        else:
            max_results = self.max_results

        max_chars_total: Union[None, Unset, int]
        if isinstance(self.max_chars_total, Unset):
            max_chars_total = UNSET
        else:
            max_chars_total = self.max_chars_total

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_blob_service_client_set is not UNSET:
            field_dict["isBlobServiceClientSet"] = is_blob_service_client_set
        if blob_service_client_display_uri is not UNSET:
            field_dict["blobServiceClientDisplayUri"] = blob_service_client_display_uri
        if is_search_client_set is not UNSET:
            field_dict["isSearchClientSet"] = is_search_client_set
        if search_client_endpoint is not UNSET:
            field_dict["searchClientEndpoint"] = search_client_endpoint
        if index_name is not UNSET:
            field_dict["indexName"] = index_name
        if index_fields is not UNSET:
            field_dict["indexFields"] = index_fields
        if use_semantic_search is not UNSET:
            field_dict["useSemanticSearch"] = use_semantic_search
        if semantic_search_configuration_name is not UNSET:
            field_dict["semanticSearchConfigurationName"] = semantic_search_configuration_name
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if max_chars_total is not UNSET:
            field_dict["maxCharsTotal"] = max_chars_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_blob_service_client_set = d.pop("isBlobServiceClientSet", UNSET)

        def _parse_blob_service_client_display_uri(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        blob_service_client_display_uri = _parse_blob_service_client_display_uri(
            d.pop("blobServiceClientDisplayUri", UNSET)
        )

        is_search_client_set = d.pop("isSearchClientSet", UNSET)

        def _parse_search_client_endpoint(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        search_client_endpoint = _parse_search_client_endpoint(d.pop("searchClientEndpoint", UNSET))

        def _parse_index_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        index_name = _parse_index_name(d.pop("indexName", UNSET))

        def _parse_index_fields(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        index_fields = _parse_index_fields(d.pop("indexFields", UNSET))

        use_semantic_search = d.pop("useSemanticSearch", UNSET)

        def _parse_semantic_search_configuration_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        semantic_search_configuration_name = _parse_semantic_search_configuration_name(
            d.pop("semanticSearchConfigurationName", UNSET)
        )

        def _parse_max_results(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_results = _parse_max_results(d.pop("maxResults", UNSET))

        def _parse_max_chars_total(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_chars_total = _parse_max_chars_total(d.pop("maxCharsTotal", UNSET))

        admin_get_acs_bot_configuration_response_dto = cls(
            is_blob_service_client_set=is_blob_service_client_set,
            blob_service_client_display_uri=blob_service_client_display_uri,
            is_search_client_set=is_search_client_set,
            search_client_endpoint=search_client_endpoint,
            index_name=index_name,
            index_fields=index_fields,
            use_semantic_search=use_semantic_search,
            semantic_search_configuration_name=semantic_search_configuration_name,
            max_results=max_results,
            max_chars_total=max_chars_total,
        )

        return admin_get_acs_bot_configuration_response_dto

from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminUpdateAcsBotConfigurationRequestDto")


@_attrs_define
class AdminUpdateAcsBotConfigurationRequestDto:
    """
    Attributes:
        is_update_blob_client (Union[Unset, bool]):
        blob_client_connection_string (Union[None, Unset, str]):
        is_update_search_client (Union[Unset, bool]):
        search_client_endpoint (Union[None, Unset, str]):
        search_client_credential (Union[None, Unset, str]):
        index_name (Union[None, Unset, str]):
        index_fields (Union[None, Unset, str]):
        use_semantic_search (Union[Unset, bool]):
        semantic_search_configuration_name (Union[None, Unset, str]):
        max_results (Union[None, Unset, int]):
        max_chars_total (Union[None, Unset, int]):
    """

    is_update_blob_client: Union[Unset, bool] = UNSET
    blob_client_connection_string: Union[None, Unset, str] = UNSET
    is_update_search_client: Union[Unset, bool] = UNSET
    search_client_endpoint: Union[None, Unset, str] = UNSET
    search_client_credential: Union[None, Unset, str] = UNSET
    index_name: Union[None, Unset, str] = UNSET
    index_fields: Union[None, Unset, str] = UNSET
    use_semantic_search: Union[Unset, bool] = UNSET
    semantic_search_configuration_name: Union[None, Unset, str] = UNSET
    max_results: Union[None, Unset, int] = UNSET
    max_chars_total: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_update_blob_client = self.is_update_blob_client

        blob_client_connection_string: Union[None, Unset, str]
        if isinstance(self.blob_client_connection_string, Unset):
            blob_client_connection_string = UNSET
        else:
            blob_client_connection_string = self.blob_client_connection_string

        is_update_search_client = self.is_update_search_client

        search_client_endpoint: Union[None, Unset, str]
        if isinstance(self.search_client_endpoint, Unset):
            search_client_endpoint = UNSET
        else:
            search_client_endpoint = self.search_client_endpoint

        search_client_credential: Union[None, Unset, str]
        if isinstance(self.search_client_credential, Unset):
            search_client_credential = UNSET
        else:
            search_client_credential = self.search_client_credential

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
        if is_update_blob_client is not UNSET:
            field_dict["isUpdateBlobClient"] = is_update_blob_client
        if blob_client_connection_string is not UNSET:
            field_dict["blobClientConnectionString"] = blob_client_connection_string
        if is_update_search_client is not UNSET:
            field_dict["isUpdateSearchClient"] = is_update_search_client
        if search_client_endpoint is not UNSET:
            field_dict["searchClientEndpoint"] = search_client_endpoint
        if search_client_credential is not UNSET:
            field_dict["searchClientCredential"] = search_client_credential
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
        is_update_blob_client = d.pop("isUpdateBlobClient", UNSET)

        def _parse_blob_client_connection_string(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        blob_client_connection_string = _parse_blob_client_connection_string(d.pop("blobClientConnectionString", UNSET))

        is_update_search_client = d.pop("isUpdateSearchClient", UNSET)

        def _parse_search_client_endpoint(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        search_client_endpoint = _parse_search_client_endpoint(d.pop("searchClientEndpoint", UNSET))

        def _parse_search_client_credential(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        search_client_credential = _parse_search_client_credential(d.pop("searchClientCredential", UNSET))

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

        admin_update_acs_bot_configuration_request_dto = cls(
            is_update_blob_client=is_update_blob_client,
            blob_client_connection_string=blob_client_connection_string,
            is_update_search_client=is_update_search_client,
            search_client_endpoint=search_client_endpoint,
            search_client_credential=search_client_credential,
            index_name=index_name,
            index_fields=index_fields,
            use_semantic_search=use_semantic_search,
            semantic_search_configuration_name=semantic_search_configuration_name,
            max_results=max_results,
            max_chars_total=max_chars_total,
        )

        return admin_update_acs_bot_configuration_request_dto

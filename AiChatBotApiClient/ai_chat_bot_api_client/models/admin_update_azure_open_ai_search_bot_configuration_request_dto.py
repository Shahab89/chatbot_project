from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminUpdateAzureOpenAISearchBotConfigurationRequestDto")


@_attrs_define
class AdminUpdateAzureOpenAISearchBotConfigurationRequestDto:
    """
    Attributes:
        is_update_blob_client (Union[Unset, bool]):
        blob_client_connection_string (Union[None, Unset, str]):
        is_update_search_client (Union[Unset, bool]):
        search_client_endpoint (Union[None, Unset, str]):
        search_client_credential (Union[None, Unset, str]):
        index_name (Union[None, Unset, str]):
        semantic_search_configuration_name (Union[None, Unset, str]):
        embedding_model_name (Union[None, Unset, str]):
        max_results (Union[None, Unset, int]):
        temperature (Union[None, Unset, float]):
        search_filter (Union[None, Unset, str]):
        search_strictness (Union[None, Unset, int]):
        search_should_restrict_result_scope (Union[None, Unset, bool]):
    """

    is_update_blob_client: Union[Unset, bool] = UNSET
    blob_client_connection_string: Union[None, Unset, str] = UNSET
    is_update_search_client: Union[Unset, bool] = UNSET
    search_client_endpoint: Union[None, Unset, str] = UNSET
    search_client_credential: Union[None, Unset, str] = UNSET
    index_name: Union[None, Unset, str] = UNSET
    semantic_search_configuration_name: Union[None, Unset, str] = UNSET
    embedding_model_name: Union[None, Unset, str] = UNSET
    max_results: Union[None, Unset, int] = UNSET
    temperature: Union[None, Unset, float] = UNSET
    search_filter: Union[None, Unset, str] = UNSET
    search_strictness: Union[None, Unset, int] = UNSET
    search_should_restrict_result_scope: Union[None, Unset, bool] = UNSET

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

        semantic_search_configuration_name: Union[None, Unset, str]
        if isinstance(self.semantic_search_configuration_name, Unset):
            semantic_search_configuration_name = UNSET
        else:
            semantic_search_configuration_name = self.semantic_search_configuration_name

        embedding_model_name: Union[None, Unset, str]
        if isinstance(self.embedding_model_name, Unset):
            embedding_model_name = UNSET
        else:
            embedding_model_name = self.embedding_model_name

        max_results: Union[None, Unset, int]
        if isinstance(self.max_results, Unset):
            max_results = UNSET
        else:
            max_results = self.max_results

        temperature: Union[None, Unset, float]
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        search_filter: Union[None, Unset, str]
        if isinstance(self.search_filter, Unset):
            search_filter = UNSET
        else:
            search_filter = self.search_filter

        search_strictness: Union[None, Unset, int]
        if isinstance(self.search_strictness, Unset):
            search_strictness = UNSET
        else:
            search_strictness = self.search_strictness

        search_should_restrict_result_scope: Union[None, Unset, bool]
        if isinstance(self.search_should_restrict_result_scope, Unset):
            search_should_restrict_result_scope = UNSET
        else:
            search_should_restrict_result_scope = self.search_should_restrict_result_scope

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
        if semantic_search_configuration_name is not UNSET:
            field_dict["semanticSearchConfigurationName"] = semantic_search_configuration_name
        if embedding_model_name is not UNSET:
            field_dict["embeddingModelName"] = embedding_model_name
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if search_filter is not UNSET:
            field_dict["searchFilter"] = search_filter
        if search_strictness is not UNSET:
            field_dict["searchStrictness"] = search_strictness
        if search_should_restrict_result_scope is not UNSET:
            field_dict["searchShouldRestrictResultScope"] = search_should_restrict_result_scope

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

        def _parse_semantic_search_configuration_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        semantic_search_configuration_name = _parse_semantic_search_configuration_name(
            d.pop("semanticSearchConfigurationName", UNSET)
        )

        def _parse_embedding_model_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        embedding_model_name = _parse_embedding_model_name(d.pop("embeddingModelName", UNSET))

        def _parse_max_results(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_results = _parse_max_results(d.pop("maxResults", UNSET))

        def _parse_temperature(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_search_filter(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        search_filter = _parse_search_filter(d.pop("searchFilter", UNSET))

        def _parse_search_strictness(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        search_strictness = _parse_search_strictness(d.pop("searchStrictness", UNSET))

        def _parse_search_should_restrict_result_scope(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        search_should_restrict_result_scope = _parse_search_should_restrict_result_scope(
            d.pop("searchShouldRestrictResultScope", UNSET)
        )

        admin_update_azure_open_ai_search_bot_configuration_request_dto = cls(
            is_update_blob_client=is_update_blob_client,
            blob_client_connection_string=blob_client_connection_string,
            is_update_search_client=is_update_search_client,
            search_client_endpoint=search_client_endpoint,
            search_client_credential=search_client_credential,
            index_name=index_name,
            semantic_search_configuration_name=semantic_search_configuration_name,
            embedding_model_name=embedding_model_name,
            max_results=max_results,
            temperature=temperature,
            search_filter=search_filter,
            search_strictness=search_strictness,
            search_should_restrict_result_scope=search_should_restrict_result_scope,
        )

        return admin_update_azure_open_ai_search_bot_configuration_request_dto

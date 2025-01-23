from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InformationSource")


@_attrs_define
class InformationSource:
    """
    Attributes:
        id (Union[None, Unset, str]):
        file_name (Union[None, Unset, str]):
        url (Union[None, Unset, str]):
        language (Union[None, Unset, str]):
        create_ticket_url (Union[None, Unset, str]):
    """

    id: Union[None, Unset, str] = UNSET
    file_name: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    language: Union[None, Unset, str] = UNSET
    create_ticket_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        file_name: Union[None, Unset, str]
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        create_ticket_url: Union[None, Unset, str]
        if isinstance(self.create_ticket_url, Unset):
            create_ticket_url = UNSET
        else:
            create_ticket_url = self.create_ticket_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if url is not UNSET:
            field_dict["url"] = url
        if language is not UNSET:
            field_dict["language"] = language
        if create_ticket_url is not UNSET:
            field_dict["createTicketUrl"] = create_ticket_url

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

        def _parse_file_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_create_ticket_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        create_ticket_url = _parse_create_ticket_url(d.pop("createTicketUrl", UNSET))

        information_source = cls(
            id=id,
            file_name=file_name,
            url=url,
            language=language,
            create_ticket_url=create_ticket_url,
        )

        return information_source

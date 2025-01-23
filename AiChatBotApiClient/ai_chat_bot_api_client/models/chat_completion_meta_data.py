from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.information_source import InformationSource


T = TypeVar("T", bound="ChatCompletionMetaData")


@_attrs_define
class ChatCompletionMetaData:
    """
    Attributes:
        tags (Union[List[str], None, Unset]):
        sources (Union[List['InformationSource'], None, Unset]):
    """

    tags: Union[List[str], None, Unset] = UNSET
    sources: Union[List["InformationSource"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tags: Union[List[str], None, Unset]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        sources: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.sources, Unset):
            sources = UNSET
        elif isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)

        else:
            sources = self.sources

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.information_source import InformationSource

        d = src_dict.copy()

        def _parse_tags(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(List[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_sources(data: object) -> Union[List["InformationSource"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in _sources_type_0:
                    sources_type_0_item = InformationSource.from_dict(sources_type_0_item_data)

                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["InformationSource"], None, Unset], data)

        sources = _parse_sources(d.pop("sources", UNSET))

        chat_completion_meta_data = cls(
            tags=tags,
            sources=sources,
        )

        return chat_completion_meta_data

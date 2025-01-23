from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_get_start_bot_bots_response_item_dto import AdminGetStartBotBotsResponseItemDto


T = TypeVar("T", bound="AdminGetStartBotBotsResponseItemDtoPagingResult")


@_attrs_define
class AdminGetStartBotBotsResponseItemDtoPagingResult:
    """
    Attributes:
        page_number (Union[Unset, int]):
        total_page_count (Union[Unset, int]):
        page_size (Union[Unset, int]):
        total_item_count (Union[Unset, int]):
        has_previous (Union[Unset, bool]):
        has_next (Union[Unset, bool]):
        items (Union[List['AdminGetStartBotBotsResponseItemDto'], None, Unset]):
    """

    page_number: Union[Unset, int] = UNSET
    total_page_count: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    total_item_count: Union[Unset, int] = UNSET
    has_previous: Union[Unset, bool] = UNSET
    has_next: Union[Unset, bool] = UNSET
    items: Union[List["AdminGetStartBotBotsResponseItemDto"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        page_number = self.page_number

        total_page_count = self.total_page_count

        page_size = self.page_size

        total_item_count = self.total_item_count

        has_previous = self.has_previous

        has_next = self.has_next

        items: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if total_page_count is not UNSET:
            field_dict["totalPageCount"] = total_page_count
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if total_item_count is not UNSET:
            field_dict["totalItemCount"] = total_item_count
        if has_previous is not UNSET:
            field_dict["hasPrevious"] = has_previous
        if has_next is not UNSET:
            field_dict["hasNext"] = has_next
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_get_start_bot_bots_response_item_dto import AdminGetStartBotBotsResponseItemDto

        d = src_dict.copy()
        page_number = d.pop("pageNumber", UNSET)

        total_page_count = d.pop("totalPageCount", UNSET)

        page_size = d.pop("pageSize", UNSET)

        total_item_count = d.pop("totalItemCount", UNSET)

        has_previous = d.pop("hasPrevious", UNSET)

        has_next = d.pop("hasNext", UNSET)

        def _parse_items(data: object) -> Union[List["AdminGetStartBotBotsResponseItemDto"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = AdminGetStartBotBotsResponseItemDto.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AdminGetStartBotBotsResponseItemDto"], None, Unset], data)

        items = _parse_items(d.pop("items", UNSET))

        admin_get_start_bot_bots_response_item_dto_paging_result = cls(
            page_number=page_number,
            total_page_count=total_page_count,
            page_size=page_size,
            total_item_count=total_item_count,
            has_previous=has_previous,
            has_next=has_next,
            items=items,
        )

        return admin_get_start_bot_bots_response_item_dto_paging_result

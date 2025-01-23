from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentUserDto")


@_attrs_define
class CurrentUserDto:
    """
    Attributes:
        id (Union[Unset, int]):
        login (Union[None, Unset, str]):
        roles (Union[List[str], None, Unset]):
        is_terms_accepted (Union[Unset, bool]):
        is_keep_chat_history (Union[Unset, bool]):
        keep_chat_history_for_days (Union[Unset, int]):
        is_keep_favorites_forever (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    login: Union[None, Unset, str] = UNSET
    roles: Union[List[str], None, Unset] = UNSET
    is_terms_accepted: Union[Unset, bool] = UNSET
    is_keep_chat_history: Union[Unset, bool] = UNSET
    keep_chat_history_for_days: Union[Unset, int] = UNSET
    is_keep_favorites_forever: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        login: Union[None, Unset, str]
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        roles: Union[List[str], None, Unset]
        if isinstance(self.roles, Unset):
            roles = UNSET
        elif isinstance(self.roles, list):
            roles = self.roles

        else:
            roles = self.roles

        is_terms_accepted = self.is_terms_accepted

        is_keep_chat_history = self.is_keep_chat_history

        keep_chat_history_for_days = self.keep_chat_history_for_days

        is_keep_favorites_forever = self.is_keep_favorites_forever

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if login is not UNSET:
            field_dict["login"] = login
        if roles is not UNSET:
            field_dict["roles"] = roles
        if is_terms_accepted is not UNSET:
            field_dict["isTermsAccepted"] = is_terms_accepted
        if is_keep_chat_history is not UNSET:
            field_dict["isKeepChatHistory"] = is_keep_chat_history
        if keep_chat_history_for_days is not UNSET:
            field_dict["keepChatHistoryForDays"] = keep_chat_history_for_days
        if is_keep_favorites_forever is not UNSET:
            field_dict["isKeepFavoritesForever"] = is_keep_favorites_forever

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        def _parse_login(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        login = _parse_login(d.pop("login", UNSET))

        def _parse_roles(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                roles_type_0 = cast(List[str], data)

                return roles_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        roles = _parse_roles(d.pop("roles", UNSET))

        is_terms_accepted = d.pop("isTermsAccepted", UNSET)

        is_keep_chat_history = d.pop("isKeepChatHistory", UNSET)

        keep_chat_history_for_days = d.pop("keepChatHistoryForDays", UNSET)

        is_keep_favorites_forever = d.pop("isKeepFavoritesForever", UNSET)

        current_user_dto = cls(
            id=id,
            login=login,
            roles=roles,
            is_terms_accepted=is_terms_accepted,
            is_keep_chat_history=is_keep_chat_history,
            keep_chat_history_for_days=keep_chat_history_for_days,
            is_keep_favorites_forever=is_keep_favorites_forever,
        )

        return current_user_dto

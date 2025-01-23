from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminUpdateBotConfigurationRequestDto")


@_attrs_define
class AdminUpdateBotConfigurationRequestDto:
    """
    Attributes:
        configuration_raw (Union[None, Unset, str]):
    """

    configuration_raw: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        configuration_raw: Union[None, Unset, str]
        if isinstance(self.configuration_raw, Unset):
            configuration_raw = UNSET
        else:
            configuration_raw = self.configuration_raw

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if configuration_raw is not UNSET:
            field_dict["configurationRaw"] = configuration_raw

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_configuration_raw(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        configuration_raw = _parse_configuration_raw(d.pop("configurationRaw", UNSET))

        admin_update_bot_configuration_request_dto = cls(
            configuration_raw=configuration_raw,
        )

        return admin_update_bot_configuration_request_dto

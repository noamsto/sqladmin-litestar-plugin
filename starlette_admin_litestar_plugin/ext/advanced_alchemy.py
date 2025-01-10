from __future__ import annotations

from datetime import timezone
from typing import Any, Optional, Type

from starlette_admin.contrib.sqla import ModelView
from starlette_admin.contrib.sqla.converters import BaseSQLAModelConverter, ModelConverter
from starlette_admin.converters import converts
from starlette_admin.fields import StringField, DateTimeField


class DateTimeUTCConverter(ModelConverter):
    # # mypy: error: Untyped decorator makes function "convert_date_time_utc" untyped  [misc]
    # @converts("DateTimeUTC")  # type: ignore[arg-type]
    # def conv_date_time_utc(self, *args: Any, **kwargs: Any) -> DateTimeUTCField:
    #     return DateTimeUTCField(**kwargs)

    @converts("GUID")
    def conv_text(self, *args: Any, **kwargs: Any) -> StringField:
        return StringField(
            **self._field_common(*args, **kwargs),
            **self._string_common(*args, **kwargs),
        )


class AuditModelView(ModelView):
    def __init__(
        self,
        model: Type[Any],
        icon: Optional[str] = None,
        name: Optional[str] = None,
        label: Optional[str] = None,
        identity: Optional[str] = None,
        converter: Optional[BaseSQLAModelConverter] = None,
    ):
        super().__init__(
            model,
            icon,
            name,
            label,
            identity,
            converter=DateTimeUTCConverter(),
        )

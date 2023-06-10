import datetime

from sqlalchemy import inspect

class CustomBaseModel:
    """ Generalize __init__, __repr__ and to_json
        Based on the models columns """

    print_filter = ()

    def __repr__(self) -> str:
        """ Define a base way to print models
            Columns inside `print_filter` are excluded """
        return "%s(%s)" % (
            self.__class__.__name__,
            {
                column: value
                for column, value in self._to_dict().items()
                if column not in self.print_filter
            },
        )

    to_json_filter = ()

    @property
    def json(self) -> dict:
        """ Define a base way to jsonify models
            Columns inside `to_json_filter` are excluded """
        return {
            column: value if not isinstance(value, datetime.date) else value.isoformat()
            for column, value in self._to_dict().items()
            if column not in self.to_json_filter
        }

    def _to_dict(self) -> dict:
        """ This would more or less be the same as a `to_json`
            But putting it in a "private" function
            Allows to_json to be overriden without impacting __repr__
            Or the other way around
            And to add filter lists """
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self.__class__).attrs
        }
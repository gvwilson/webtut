"""Data generation utilities."""

from datetime import date, timedelta
import json
import random

from pydantic import BaseModel


def ensure_id_generator(cls, stem, digits):
    """Ensure class has ID generator."""
    if not hasattr(cls, "_id_gen"):
        cls._id_gen = id_gen(stem, digits)


def id_gen(stem, digits):
    """Generate unique IDs of the form 'stemDDDD'."""
    i = 1
    while True:
        temp = str(i)
        assert len(temp) <= digits, f"ID generation overflow {stem}: {i}"
        yield f"{stem}{temp.zfill(digits)}"
        i += 1


def json_dump(obj, indent=2):
    """Dump as JSON with custom serializer."""
    return json.dumps(obj, indent=indent, default=_serialize_json)


def random_date(date_min, date_max):
    """Select random date in range (inclusive)."""
    days = (date_max - date_min).days
    days = random.randint(0, days + 1)
    return date_min + timedelta(days=days)


def _serialize_json(obj):
    """Custom JSON serializer."""
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, BaseModel):
        return obj.model_dump()
    raise TypeError(f"Type {type(obj)} not serializable")

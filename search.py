"""Search functions for the sample record collection."""

from collections.abc import Iterable


def search_records(
    records: Iterable[dict[str, str]], search_term: str
) -> list[dict[str, str]]:
    """Return records containing the search term in any field, ignoring case."""
    normalized_term = search_term.strip().casefold()
    if not normalized_term:
        return []

    return [
        record
        for record in records
        if any(normalized_term in value.casefold() for value in record.values())
    ]

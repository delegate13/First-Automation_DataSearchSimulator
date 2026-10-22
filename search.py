"""Search functions for the sample record collection."""

from collections.abc import Iterable


def _record_matches_search(record: dict[str, str], normalized_term: str) -> bool:
    """Return whether the term appears in any text field of one record."""
    return any(
        normalized_term in field_value.casefold()
        for field_value in record.values()
    )


def search_records(
    records: Iterable[dict[str, str]], search_term: str
) -> list[dict[str, str]]:
    """Find records containing the search term in any field, ignoring case."""
    # Trim extra spaces and make comparisons case-insensitive.
    normalized_term = search_term.strip().casefold()
    if not normalized_term:
        # An empty search would match every record, so treat it as no results.
        return []

    # Keep a record when the term appears in at least one of its text values.
    return [
        record
        for record in records
        if _record_matches_search(record, normalized_term)
    ]

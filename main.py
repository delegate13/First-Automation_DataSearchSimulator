"""Console entry point for the Data Search Simulator."""

from data import RECORDS
from search import search_records
from utils import (
    display_search_summary,
    display_welcome_message,
    get_search_term,
    simulate_search_delay,
)


def main() -> None:
    display_welcome_message()
    search_term = get_search_term()

    print(f'\nSearching for "{search_term}"...')
    simulate_search_delay()

    matches = search_records(RECORDS, search_term)
    display_search_summary(search_term, matches)


if __name__ == "__main__":
    main()

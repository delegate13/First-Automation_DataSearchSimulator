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
    # Show the user what the program does before asking for input.
    display_welcome_message()
    # This helper keeps asking until the user enters a non-empty search term.
    search_term = get_search_term()

    # The pause is only for demonstration; the data is already available locally.
    print(f'\nSearching for "{search_term}"...')
    simulate_search_delay()

    # Search the sample records, then show the matches in a readable format.
    matching_records = search_records(RECORDS, search_term)
    display_search_summary(search_term, matching_records)


if __name__ == "__main__":
    # Run the program only when this file is started directly, not when imported.
    main()

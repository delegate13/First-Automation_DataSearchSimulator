"""Console input, presentation, and delay helpers."""

import time
from collections.abc import Sequence

SEARCH_DELAY_SECONDS = 2.5


def display_welcome_message() -> None:
    """Display the application welcome banner."""
    print("=" * 50)
    print("Welcome to the Data Search Simulator")
    print("=" * 50)


def get_search_term() -> str:
    """Prompt until the user enters a non-blank search term."""
    while True:
        # strip() removes spaces at the beginning and end of the user's input.
        search_term = input("Enter a search term: ").strip()
        if search_term:
            # Return the valid value to the part of the program that called us.
            return search_term
        # If the input was empty, explain the problem and repeat the loop.
        print("Error: the search term cannot be blank. Please try again.")


def simulate_search_delay() -> None:
    """Pause briefly to simulate retrieving search results."""
    # sleep() pauses execution for the given number of seconds.
    time.sleep(SEARCH_DELAY_SECONDS)


def display_search_summary(
    search_term: str, matching_records: Sequence[dict[str, str]]
) -> None:
    """Print the search term, result count, and matching records."""
    # Show a small heading and how many records matched.
    print("\nSearch summary")
    print("-" * 50)
    print(f"Search term: {search_term}")
    print(f"Matching records: {len(matching_records)}")

    if not matching_records:
        # There is nothing else to display, so leave this function now.
        print("No matching records were found. Try a different search term.")
        return

    # Print each matching dictionary using its known fields.
    print("Results:")
    for record in matching_records:
        print(
            f"- [{record['id']}] {record['title']} "
            f"({record['category']}): {record['description']}"
        )

"""Console input, presentation, and delay helpers."""

import time
from collections.abc import Sequence


def display_welcome_message() -> None:
    """Display the application welcome banner."""
    print("=" * 50)
    print("Welcome to the Data Search Simulator")
    print("=" * 50)


def get_search_term() -> str:
    """Prompt until the user enters a non-blank search term."""
    while True:
        search_term = input("Enter a search term: ").strip()
        if search_term:
            return search_term
        print("Error: the search term cannot be blank. Please try again.")


def simulate_search_delay() -> None:
    """Pause briefly to simulate retrieving search results."""
    time.sleep(2.5)


def display_search_summary(
    search_term: str, matches: Sequence[dict[str, str]]
) -> None:
    """Print the search term, result count, and matching records."""
    print("\nSearch summary")
    print("-" * 50)
    print(f"Search term: {search_term}")
    print(f"Matching records: {len(matches)}")

    if not matches:
        print("No matching records were found. Try a different search term.")
        return

    print("Results:")
    for record in matches:
        print(
            f"- [{record['id']}] {record['title']} "
            f"({record['category']}): {record['description']}"
        )

"""Fetch sample Geometry Dash levels and print metadata."""

import gd

NUM_LEVELS = 3
SEARCH_QUERY = "demon"


def create_client() -> gd.Client:
    return gd.Client()


async def fetch_sample_levels(client: gd.Client, query: str, count: int) -> list:
    levels = []
    for level in await client.search_levels(query):
        levels.append(level)
        if len(levels) >= count:
            break
    return levels


def level_to_dict(level: gd.Level) -> dict:
    creator = level.creator.name if level.creator else "Unknown"
    return {
        "name": level.name,
        "id": level.id,
        "creator": creator,
        "difficulty": str(level.difficulty),
        "downloads": level.downloads,
    }


def print_level(info: dict) -> None:
    print("-" * 40)
    print(f"Name:       {info['name']}")
    print(f"ID:         {info['id']}")
    print(f"Creator:    {info['creator']}")
    print(f"Difficulty: {info['difficulty']}")
    print(f"Downloads:  {info['downloads']:,}")


def print_levels(levels: list) -> None:
    if not levels:
        print("No levels found.")
        return

    print(f"\n{len(levels)} level(s):\n")
    for level in levels:
        print_level(level_to_dict(level))


async def main() -> None:
    client = create_client()
    levels = await fetch_sample_levels(client, SEARCH_QUERY, NUM_LEVELS)
    print_levels(levels)


if __name__ == "__main__":
    create_client().run(main())

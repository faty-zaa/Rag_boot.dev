import argparse
from lib.search_utils import Data
from lib.keyword_search import Search


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Searching for: QUERY")

    args = parser.parse_args()
    data = Data().get_data
    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")
            queries = Search.search_keyword(data, args.query)
            i = 1
            for query in queries.values():
                if i < 6:
                    print(f"{i}. {query} {i}")
                    i += 1
                else:
                    break
                
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
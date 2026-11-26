import argparse
from lib.search_utils import load_dataset
from lib.keyword_search import load_command, find_title_by_query, print_results, build_command


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")
    build_parser = subparsers.add_parser("build", help="Build the inverted index")
    
    args = parser.parse_args()

    match args.command:
        case "search":
            query = args.query
            print("Searching for: " + query)
            movies = load_command()
            results = find_title_by_query(movies, query)
            print_results(results)
            pass
        case "build":
            build_command()
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()

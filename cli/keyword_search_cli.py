import argparse
from lib.search_utils import load_dataset
from lib.keyword_search import InvertedIndex, load_command, find_title_by_query, print_results, build_command, preprocess_one_term


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")
    build_parser = subparsers.add_parser("build", help="Build the inverted index")
    tf_parser = subparsers.add_parser("tf", help="Return the term frecuency for a given term and document")
    tf_parser.add_argument("doc_id", type=str, help="Document from which to check term frecuency")
    tf_parser.add_argument("term", type=str, help="Term to search for in document")
    
    args = parser.parse_args()
    movies = InvertedIndex()

    match args.command:
        case "search":
            query = args.query
            print("Searching for: " + query)
            load_command(movies)
            results = find_title_by_query(movies, query)
            print_results(results)
            pass
        case "build":
            build_command(movies)
        case "tf":
            doc_id = int(args.doc_id)
            term = args.term
            load_command(movies)
            new_term = preprocess_one_term(term)
            tf = movies.get_tf(doc_id, new_term)
            print(tf)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()

import sys

import dns.resolver

resolver = dns.resolver.Resolver()


def dns_brute(file: str, target: str) -> None:
    try:
        with open(file, "r") as wordlist:
            subdomains = wordlist.read().splitlines()

    except:
        print("wordlist file not found")
        sys.exit()

    for subdomain in subdomains:
        try:
            sub_target = f"{subdomain}.{target}"
            results = resolver.resolve(sub_target, "A")

            for result in results:
                print(f"{sub_target}: {result}")

        except:
            pass

    return None


def main() -> None:
    import argparse

    parser: object = argparse.ArgumentParser(
        prog="dnsbrute",
        description="Brute DNS enumerator",
        epilog="Enumerates the given DNS using an internal wordlist",
    )

    parser.add_argument(
        "-w",
        "--wordlist",
        type=str,
        default="/usr/share/wordlists/dirb/common.txt",
        help="The wordlist that should be used for enumerate, default=common.txt",
        required=False,
    )
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        help="The target DNS that should be enumerated",
        required=True,
    )

    args: object = parser.parse_args()

    dns_brute(file=args.wordlist, target=args.target)

    return None


if __name__ == "__main__":
    main()

from statistics import median

# EDITABLE INPUTS
# Frozen case: December 31, 2024 prices and FY2024 total GAAP diluted EPS.
target = {"ticker": "ABG", "price": 243.03, "eps": 21.50}

peers = [
    {"ticker": "AN", "price": 169.84, "eps": 16.92},
    {"ticker": "GPI", "price": 421.48, "eps": 36.81},
]


def positive_number(value):
    """Accept only finite, positive numbers."""
    from math import isfinite

    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and isfinite(value)
        and value > 0
    )


def main():
    target_ticker = target["ticker"].strip().upper()
    target_eps = target.get("eps")
    target_price = target.get("price")
    target_eps_valid = positive_number(target_eps)

    print(f"Target: {target_ticker}")

    if positive_number(target_price) and target_eps_valid:
        print(f"Target observed P/E: {target_price / target_eps:.6f}x")
    else:
        print("Target observed P/E: not meaningful")

    if not target_eps_valid:
        print("Target implied prices: not meaningful (invalid EPS)")

    # Deduplicate by ticker and exclude the target.
    seen = set()
    valid_peers = []

    for peer in peers:
        ticker = str(peer.get("ticker") or "").strip().upper()

        if not ticker:
            print("Peer excluded: missing ticker")
            continue

        if ticker == target_ticker:
            print(f"{ticker}: excluded because it is the target")
            continue

        if ticker in seen:
            print(f"{ticker}: duplicate excluded")
            continue

        seen.add(ticker)
        price = peer.get("price")
        eps = peer.get("eps")

        if not positive_number(price) or not positive_number(eps):
            print(f"{ticker} P/E: not meaningful (invalid price or EPS)")
            continue

        pe = price / eps
        valid_peers.append((ticker, pe))
        print(f"{ticker} P/E: {pe:.6f}x")

    if not valid_peers:
        print("No usable peers.")
        return

    multiples = [pe for ticker, pe in valid_peers]
    median_pe = median(multiples)

    print(f"Peer median P/E: {median_pe:.6f}x")

    if not target_eps_valid:
        for ticker, _ in valid_peers:
            print(f"Remove {ticker}: implied price not meaningful")
        return

    full_estimate = median_pe * target_eps

    if len(valid_peers) == 1:
        print(f"Reference estimate: ${full_estimate:.2f}")
        print("One valid peer: no range.")
    else:
        low_price = min(multiples) * target_eps
        high_price = max(multiples) * target_eps

        print(f"Minimum implied price: ${low_price:.2f}")
        print(f"Median implied price: ${full_estimate:.2f}")
        print(f"Maximum implied price: ${high_price:.2f}")
        print(f"Peer-implied range: ${low_price:.2f}-${high_price:.2f}")

    print("\nLeave-one-peer-out checks:")

    for removed_ticker, _ in valid_peers:
        remaining = [
            pe for ticker, pe in valid_peers
            if ticker != removed_ticker
        ]

        if not remaining:
            print(f"Remove {removed_ticker}: no estimate; no peers remain")
            continue

        remaining_estimate = median(remaining) * target_eps
        change = remaining_estimate - full_estimate

        print(
            f"Remove {removed_ticker}: "
            f"remaining median-implied price = ${remaining_estimate:.2f}; "
            f"change = {change:+.2f} USD"
        )

        if len(remaining) == 1:
            print("  One remaining peer: reference estimate, no range.")


if __name__ == "__main__":
    main()
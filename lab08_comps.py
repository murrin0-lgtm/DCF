"""Lab 08: frozen, sourced eBay comparison. Standard library only.

Run: python lab08_comps.py
Sources and qualifications are recorded in lab08_notes.md.
No data downloads, cash/debt bridge, or rounded intermediate calculations.
"""

from math import isfinite
from statistics import median

# EDITABLE INPUTS: USD per share, FY2025 total GAAP diluted EPS.
comparison_date = "2026-09-16"
target = {"ticker": "EBAY", "price": 109.17, "eps": 4.34}
peers = [
    {"ticker": "ETSY", "price": 73.46, "eps": 1.39, "decision": "qualify"},
    {"ticker": "MELI", "price": 1839.71, "eps": 39.40, "decision": "qualify"},
]


def positive(value):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and isfinite(value) and value > 0)


def analyze(company, candidates):
    """Return full-precision results and reasons for omitted candidates."""
    ticker = str(company.get("ticker") or "").strip().upper()
    seen = set()
    valid = []
    messages = []
    for candidate in candidates:
        symbol = str(candidate.get("ticker") or "").strip().upper()
        if not symbol:
            messages.append("Candidate excluded: missing ticker.")
            continue
        if symbol == ticker:
            messages.append(f"{symbol}: target excluded from its own peers.")
            continue
        if symbol in seen:
            messages.append(f"{symbol}: duplicate excluded (first entry retained).")
            continue
        seen.add(symbol)
        if candidate.get("decision", "use").lower() not in ("use", "qualify"):
            messages.append(f"{symbol}: excluded by peer policy.")
            continue
        price, eps = candidate.get("price"), candidate.get("eps")
        if not positive(price) or not positive(eps):
            messages.append(f"{symbol}: P/E not meaningful; missing/nonpositive/nonfinite price or EPS.")
            continue
        valid.append((symbol, price / eps))

    eps = company.get("eps")
    multiples = [pe for _, pe in valid]
    middle = median(multiples) if multiples else None
    estimate = middle * eps if middle is not None and positive(eps) else None
    removals = []
    for symbol, _ in valid:
        remaining = [pe for name, pe in valid if name != symbol]
        remaining_price = median(remaining) * eps if remaining and positive(eps) else None
        change = remaining_price - estimate if remaining_price is not None else None
        removals.append((symbol, remaining_price, change, len(remaining)))
    return {"valid": valid, "messages": messages, "median": middle,
            "estimate": estimate, "removals": removals}


def main():
    result = analyze(target, peers)
    print(f"LAB 08: {target['ticker']} | closing prices {comparison_date}")
    print("Basis: USD/share; FY2025 total reported GAAP diluted EPS.")
    print("Qualified peers: see lab08_notes.md before interpreting the range.")
    if positive(target.get("price")):
        print(f"Target closing price: ${target['price']:.2f}")
    else:
        print("Target market-price comparison: not meaningful.")
    if positive(target.get("price")) and positive(target.get("eps")):
        print(f"Target observed P/E (excluded from peer median): {target['price'] / target['eps']:.6f}x")
    else:
        print("Target observed P/E: not meaningful.")
    for message in result["messages"]:
        print(message)
    for symbol, pe in result["valid"]:
        print(f"{symbol} P/E: {pe:.6f}x")
    if not result["valid"]:
        print("No usable peers; no estimate or range.")
        return
    print(f"Peer median P/E: {result['median']:.6f}x")
    if result["estimate"] is None:
        print("Target implied prices and dollar changes: not meaningful (invalid target EPS).")
        return
    estimates = [pe * target["eps"] for _, pe in result["valid"]]
    if len(estimates) == 1:
        print(f"Single-peer reference estimate: ${result['estimate']:.2f}; no range.")
    else:
        print(f"Minimum implied price: ${min(estimates):.2f}")
        print(f"Median implied price: ${result['estimate']:.2f}")
        print(f"Maximum implied price: ${max(estimates):.2f}")
        print(f"Mechanical peer-implied range: ${min(estimates):.2f}-${max(estimates):.2f}")
    print("\nLeave-one-peer-out checks (changes use unrounded values):")
    for symbol, estimate, change, count in result["removals"]:
        if estimate is None:
            print(f"Remove {symbol}: no estimate; no usable peers remain.")
        else:
            print(f"Remove {symbol}: ${estimate:.2f}; change {change:+.2f} USD.")
            if count == 1:
                print("  One remaining peer: reference estimate, no range.")
    print("\nDCF: no completed eBay range available; training DCF is not eBay.")
    print("Draft conclusion: watch-defer pending comparability and DCF checks.")


if __name__ == "__main__":
    main()

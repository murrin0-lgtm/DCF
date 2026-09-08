# INPUTS — edit these values.
# Cash amounts are in USD millions; diluted shares are in millions.
starting_fcff = 100.0
growth_rates = [0.08, 0.06, 0.05, 0.04, 0.03]
wacc = 0.10
terminal_growth = 0.03
non_operating_cash = 50.0
debt = 300.0
diluted_shares = 50.0

if terminal_growth >= wacc:
    raise SystemExit("Error: terminal growth must be less than WACC.")
if len(growth_rates) != 5:
    raise SystemExit("Error: enter exactly five yearly growth rates.")
if wacc <= -1:
    raise SystemExit("Error: WACC must be greater than -100%.")
if diluted_shares <= 0:
    raise SystemExit("Error: diluted shares must be positive.")

# Forecast five annual cash flows.
annual_fcff = []
fcff = starting_fcff

for growth in growth_rates:
    fcff *= 1 + growth
    annual_fcff.append(fcff)

# Discount each cash flow from its year-end to today.
pv_explicit = sum(
    cash_flow / (1 + wacc) ** year
    for year, cash_flow in enumerate(annual_fcff, start=1)
)

# Gordon-growth terminal value at the end of Year 5.
terminal_value = (
    annual_fcff[-1] * (1 + terminal_growth)
    / (wacc - terminal_growth)
)
pv_terminal = terminal_value / (1 + wacc) ** len(growth_rates)

enterprise_value = pv_explicit + pv_terminal
equity_value = enterprise_value + non_operating_cash - debt
value_per_share = equity_value / diluted_shares

if enterprise_value == 0:
    raise SystemExit(
        "Error: enterprise value is zero; terminal value share is undefined."
    )

terminal_share = pv_terminal / enterprise_value

# Print exactly twelve labelled lines, each to four decimal places.
for year, cash_flow in enumerate(annual_fcff, start=1):
    print(f"Year {year} FCFF (USD millions): {cash_flow:.4f}")

print(f"PV of five explicit FCFF (USD millions): {pv_explicit:.4f}")
print(f"Terminal value at Year 5 (USD millions): {terminal_value:.4f}")
print(f"PV of terminal value (USD millions): {pv_terminal:.4f}")
print(f"Enterprise value (USD millions): {enterprise_value:.4f}")
print(f"Equity value (USD millions): {equity_value:.4f}")
print(f"Value per diluted share (USD): {value_per_share:.4f}")
print(
    "PV of terminal value as share of enterprise value (%): "
    f"{terminal_share * 100:.4f}"
)
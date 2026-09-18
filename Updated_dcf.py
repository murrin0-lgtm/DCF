"""eBay legacy FCFF DCF plus Depop transaction-value proxy. Standard library only.
Run: python dcf.py | training check: python dcf.py --training
Sources and limitations: lab08_completion_append.md.
"""
import argparse
from math import isfinite

# EDITABLE EBAY INPUTS. Cash amounts and share counts in millions.
valuation_date = '2026-09-16'
operating_cash_flow = 2009.0       # FY2025 continuing operations
interest_paid = 256.0             # FY2025 cash paid for interest
capital_expenditure = 525.0       # FY2025 property/equipment purchases
tax_rate = 0.21                   # assumed tax shield, not actual effective rate
interest_income = 265.0           # FY2025 accrued interest; proxy for cash receipts
remove_investment_income = True   # avoid capitalizing income on separately valued assets
growth_rates = [0.05, 0.04, 0.04, 0.03, 0.03]  # forecast, not company guidance
terminal_growth = 0.025           # assumed long-run nominal growth
cash_reported = 2310.0            # June 30, 2026
short_term_investments = 997.0     # June 30, Note 5, fair value
long_term_debt_investments = 1544.0  # June 30, Note 5, fair value
equity_investments = 773.0         # June 30, Note 5, carrying-value proxy
operating_cash_reserve = 1000.0   # judgement, not reported required cash
depop_cash_paid = 1400.0          # July 30 close, Q2 10-Q Note 3
depop_equity_value = 1400.0       # acquisition-cost proxy, NOT an independent DCF
other_net_cash_movement = 0.0     # assume other June-to-valuation flows net to zero
debt = 6735.0                    # June 30 carrying value as proxy
diluted_shares = 468.0            # FY2025 diluted weighted average, lab convention
target_price = 109.17             # September 16 regular-session close, USD/share
risk_free_rate = 0.0501           # September 16 Treasury 10-year yield
beta = 1.0                       # assumed market-level risk, not measured eBay beta
equity_risk_premium = 0.05        # lab convention
pretax_cost_of_debt = 0.05125     # 2035 bond coupon proxy, not current yield
shares_for_market_cap = 445.0    # June common shares as September proxy

# Derived inputs: no valuation answers are hard-coded.
lab_formula_fcff = operating_cash_flow + interest_paid * (1-tax_rate) - capital_expenditure
starting_fcff = lab_formula_fcff - (interest_income * (1-tax_rate) if remove_investment_income else 0)
non_operating_cash = (cash_reported + short_term_investments + long_term_debt_investments
                     - operating_cash_reserve - depop_cash_paid + other_net_cash_movement)
other_equity_assets = equity_investments + depop_equity_value
market_equity = target_price * shares_for_market_cap
cost_of_equity = risk_free_rate + beta * equity_risk_premium
after_tax_cost_of_debt = pretax_cost_of_debt * (1-tax_rate)
wacc = (market_equity*cost_of_equity + debt*after_tax_cost_of_debt)/(market_equity+debt)
wacc_values = [wacc-0.01, wacc, wacc+0.01]
terminal_growth_values = [0.015, 0.025, 0.035]
reverse_brackets = [(-0.05, 0.10), (-0.05, 0.40)]  # original, then explicit expanded test


def inputs(training=False):
    if training:
        return dict(start=100.0, growth=[.08,.06,.05,.04,.03], wacc=.10, terminal=.03,
                    cash=50.0, assets=0.0, debt=300.0, shares=50.0, price=30.0,
                    rates=[.09,.10,.11], terminals=[.02,.03,.04], brackets=[(-.05,.10)], training=True)
    return dict(start=starting_fcff, growth=growth_rates, wacc=wacc, terminal=terminal_growth,
                cash=non_operating_cash, assets=other_equity_assets, debt=debt, shares=diluted_shares,
                price=target_price, rates=wacc_values, terminals=terminal_growth_values,
                brackets=reverse_brackets, training=False)


def value(p, rate=None, terminal=None, shift=0.0):
    rate = p['wacc'] if rate is None else rate
    terminal = p['terminal'] if terminal is None else terminal
    if not all(isfinite(x) for x in [p['start'],rate,terminal,shift,p['cash'],p['assets'],p['debt'],p['shares'],*p['growth']]):
        raise ValueError('All model inputs must be finite numbers.')
    if len(p['growth']) != 5:
        raise ValueError('Enter exactly five annual growth rates.')
    if terminal >= rate:
        raise ValueError('Terminal growth must be below WACC.')
    if rate <= -1 or terminal <= -1:
        raise ValueError('WACC and terminal growth must exceed -100%.')
    if p['shares'] <= 0:
        raise ValueError('Diluted shares must be positive.')
    if p['start'] <= 0:
        raise ValueError('This growth-path model needs positive FCFF; use an explicit path for losses.')
    if any(g+shift <= -1 for g in p['growth']):
        raise ValueError('Annual growth must exceed -100%.')
    flows = []
    cf = p['start']
    for g in p['growth']:
        cf *= 1+g+shift
        flows.append(cf)
    explicit = sum(cf/(1+rate)**year for year,cf in enumerate(flows,1))
    tv = flows[-1]*(1+terminal)/(rate-terminal)
    pv_tv = tv/(1+rate)**5
    ev = explicit+pv_tv
    equity = ev+p['cash']+p['assets']-p['debt']
    return dict(flows=flows, explicit=explicit, tv=tv, pv_tv=pv_tv, ev=ev,
                equity=equity, price=equity/p['shares'], tv_share=pv_tv/ev)


def reverse(p, low, high):
    if not all(isfinite(x) for x in (low,high,p['price'])) or low >= high:
        return 'Invalid bracket or target price.'
    if any(g+low <= -1 or g+high <= -1 for g in p['growth']):
        return 'Invalid bracket: an annual growth rate reaches -100% or below.'
    left = value(p,shift=low)['price']-p['price']
    right = value(p,shift=high)['price']-p['price']
    if abs(left) < 1e-8: return low
    if abs(right) < 1e-8: return high
    if left*right > 0: return 'No solution in this bracket.'
    for _ in range(200):
        mid = (low+high)/2
        error = value(p,shift=mid)['price']-p['price']
        if abs(error) < 1e-8: return mid
        if left*error < 0:
            high = mid
        else:
            low,left = mid,error
    return 'No converged solution; no bound returned as an answer.'


def report(p):
    r=value(p)
    # Original 12 numeric lines. Enterprise value covers legacy operations in EBAY mode.
    for year,cf in enumerate(r['flows'],1): print(f'Year {year} FCFF (USD millions): {cf:.4f}')
    print(f"PV of five explicit FCFF (USD millions): {r['explicit']:.4f}")
    print(f"Terminal value at Year 5 (USD millions): {r['tv']:.4f}")
    print(f"PV of terminal value (USD millions): {r['pv_tv']:.4f}")
    print(f"Enterprise value (USD millions): {r['ev']:.4f}")
    print(f"Equity value (USD millions): {r['equity']:.4f}")
    print(f"Value per diluted share (USD): {r['price']:.4f}")
    print(f"PV of terminal value as share of enterprise value (%): {r['tv_share']*100:.4f}")
    label='TRAINING' if p['training'] else 'EBAY SCENARIO'
    if not p['training']:
        print(f'\nScope: {valuation_date}; five forward annual periods, end-of-year discounting.')
        print('Enterprise value above covers legacy operations; Depop equity is added separately.')
        print(f'Lab-formula FCFF: {lab_formula_fcff:.4f}; adjusted model FCFF: {p["start"]:.4f}')
        print(f'Estimated non-operating liquid assets after reserve/payment: {p["cash"]:.4f}')
        print(f'Other equity assets: {p["assets"]:.4f} (investments plus Depop value proxy).')
        print(f'WACC: {p["wacc"]:.8%}; market price: ${p["price"]:.2f}')
        ratio=r['price']/p['price']
        band='inside' if .5 <= ratio <= 2 else 'outside'
        print(f'Reasonableness: value/market price = {ratio:.4f}x, {band} 0.5x-2x band.')
    print(f'\nSENSITIVITY GRID -- {label} (USD per share)')
    print('WACC / g'+''.join(f'{g:>12.2%}' for g in p['terminals']))
    values=[]
    for rate in p['rates']:
        row=f'{rate:<10.4%}'
        for g in p['terminals']:
            try: price=value(p,rate,g)['price']
            except ValueError: row+=f'{"invalid":>12}'
            else:
                values.append(price)
                row+=f'{price:>12.2f}'
        print(row)
    if values: print(f'Sensitivity range: ${min(values):.2f}-${max(values):.2f}')
    print(f'\nREVERSE DCF -- {label}; target ${p["price"]:.2f}')
    print('Solved variable: uniform percentage-point shift to the five legacy growth rates.')
    print(f'Fixed: FCFF={p["start"]:.4f}; WACC={p["wacc"]:.8%}; terminal={p["terminal"]:.4%}; '
          f'cash={p["cash"]:.4f}; assets={p["assets"]:.4f}; debt={p["debt"]:.4f}; shares={p["shares"]:.4f}.')
    for low,high in p['brackets']:
        print(f'Tested bracket: {low*100:+.2f} to {high*100:+.2f} percentage points.')
        solved=reverse(p,low,high)
        if isinstance(solved,str): print(solved)
        else:
            print(f'Solved shift: {solved*100:+.4f} percentage points')
            print('Implied growth rates: '+', '.join(f'{g+solved:.4%}' for g in p['growth']))
            print(f'Check price: ${value(p,shift=solved)["price"]:.4f}')
            break


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--training',action='store_true')
    args=parser.parse_args()
    try: report(inputs(args.training))
    except ValueError as exc: raise SystemExit(f'Error: {exc}')

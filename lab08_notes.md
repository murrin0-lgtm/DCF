# Lab 08 — eBay Comparable-Company Valuation

Target: eBay Inc. (EBAY)  
Comparison date: September 16, 2026, regular-session close (4:00 p.m. Eastern)  
Prepared: September 17, 2026  
Calculator: `lab08_comps.py` — standard library only; frozen inputs, no downloads.

## Preparation and ownership

This is an AI-assisted draft, including the initial policy, research, interpretation, and proposed judgments below. The sources were accessed by the assistant. It does not claim that I independently wrote the initial policy, personally opened every source, consulted a second AI independently, or completed a partner discussion. Those course activities remain for me to review and complete. This version consolidates the earlier Lab 8 draft; it should replace that draft rather than be appended to it.

The Week 3 company DCF is incomplete. The validated $27.4974 training result is not an eBay valuation. This limitation is retained explicitly; no missing company range is invented.

## Question and initial policy

What would eBay's share be worth at defensible marketplace-company P/E multiples, and what can this comparison establish without a completed company DCF?

eBay connects buyers and sellers and earns marketplace fees and advertising revenue. The comparison should emphasize operating economics rather than an industry label. [eBay 2025 10-K, Item 1 and MD&A](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm).

The AI-assisted policy recorded before candidate selection was to investigate listed operating companies whose main businesses connect third-party buyers and sellers and earn transaction or seller-service fees. Assess product focus, geography, growth, profitability, inventory ownership, and physical infrastructure. Qualify material differences; exclude fundamentally different businesses or unverifiable inputs from the numerical comparison. Positive annual reported diluted EPS is necessary for this positive P/E exercise.

Rejection evidence would include predominantly inventory-owning retail economics, unrelated earnings dominating the business, nonpositive annual EPS, or price/EPS data that cannot be put on compatible currency and share bases. No policy changes were made to select a preferred numerical answer.

P/E = price per share / annual EPS. Implied target price = peer P/E × target EPS. A low multiple can reflect weak growth, risk, or temporarily high earnings; it is not automatically a bargain. This method yields equity value per share directly: do not add cash or subtract debt.

## Two candidate decisions

| Candidate | Decision | Business fit | Material qualification |
|---|---|---|---|
| Etsy (ETSY) | Qualify and include | Marketplace fees and seller services resemble the target's economics. | Creative-goods focus; historical earnings include divested businesses and an impairment. |
| MercadoLibre (MELI) | Qualify and include | Third-party marketplace, advertising and payments activities. | Latin American geography, logistics, first-party sales, and lending/financial services change the earnings mix. |

**Etsy evidence:** [2025 10-K](https://investors.etsy.com/sec-filings/all-sec-filings/content/0001370637-26-000019/etsy-20251231.htm), Item 1, pages 1–2, “About our Company” and “How We Make Money.” Note 6 reports a $101.7 million Reverb goodwill impairment. The original annual results include Depop and part-year Reverb. Depressed reported earnings can inflate P/E; I retain GAAP EPS and flag this rather than substitute adjusted earnings.

**MercadoLibre evidence:** [2025 10-K](https://http2.mlstatic.com/storage/ml-cms-backend/cms-documents-prod/sec/0001099590/0001099590-26-000006/form10-K-0001099590-26-000006.pdf), Item 1, pages 5–6. Most marketplace GMV comes from third-party sellers; first-party sales are less than 10% of GMV. Mercado Pago also provides off-platform payments and credit; Mercado Envios provides logistics. Consolidated EPS is therefore not a pure marketplace measure. Qualification permits a limited comparison; it does not establish equal deserved multiples.

Neither candidate was excluded. If later evidence warrants exclusion, preserve the candidate and reason here and rerun the calculator.

## Frozen inputs and audit trail

All prices and EPS are USD per common share. Earnings are total annual reported GAAP diluted EPS, not adjusted EPS, a single quarter, or a trailing-four-quarter estimate. All fiscal years ended December 31, 2025. The annual earnings were public before the comparison date. Use each price table's **Close** column, not a dividend-adjusted total-return price; do not introduce a stock-split mismatch.

| Role/company | Close, September 16, 2026 | FY2025 diluted EPS | Annual results publication | Earnings source and locator |
|---|---:|---:|---|---|
| Target: EBAY | $109.17 | $4.34 | February 18, 2026; 10-K filed February 19 | [10-K](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm), Note 2, page 76, total diluted net-income-per-share row; [release](https://investors.ebayinc.com/investor-news/press-release-details/2026/eBay-Inc--Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx) |
| Qualified peer: ETSY | $73.46 | $1.39 | February 19, 2026 | [10-K](https://investors.etsy.com/sec-filings/all-sec-filings/content/0001370637-26-000019/etsy-20251231.htm), Note 4, page 84, diluted EPS row |
| Qualified peer: MELI | $1,839.71 | $39.40 | February 24, 2026 | [10-K](https://http2.mlstatic.com/storage/ml-cms-backend/cms-documents-prod/sec/0001099590/0001099590-26-000006/form10-K-0001099590-26-000006.pdf), Consolidated Statements of Income, page 78, annual diluted EPS; [release-date confirmation](https://www.nasdaq.com/press-release/mercadolibre-inc-reports-fourth-quarter-and-full-year-2025-financial-results-2026-02) |

Price locators: September 16, 2026 row, **Close** column in [EBAY history](https://stockanalysis.com/stocks/ebay/history/), [ETSY history](https://stockanalysis.com/stocks/etsy/history/), and [MELI history](https://stockanalysis.com/stocks/meli/history/). These are named secondary market-data sources. Nasdaq was attempted first; the historical tables were unavailable to the research tool. Closing prices were corroborated with [EBAY Yahoo history](https://ca.finance.yahoo.com/quote/EBAY/history/), [ETSY Yahoo history](https://ca.finance.yahoo.com/quote/ETSY/history/), and [MELI KlickAnalytics history](https://www.klickanalytics.com/symbol_performance?s=MELI). Source retrieval occurred September 17; the selected observations are September 16, not September 17 prices.

The business perimeter is not identical across dates: FY2025 earnings predate the July 2026 transfer of Depop from Etsy to eBay. Keeping total GAAP EPS consistent does not eliminate that economic mismatch. [eBay Q2 2026 10-Q, “Acquisition of Depop Limited”](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000177/ebay-20260630.htm).

## Calculated results

| Calculation | Result |
|---|---:|
| EBAY observed P/E — not included in peer median | 25.154378× |
| ETSY P/E | 52.848921× |
| MELI P/E | 46.693147× |
| Peer median P/E | 49.771034× |
| EBAY implied price using MELI | $202.65 |
| EBAY implied price at peer median | $216.01 |
| EBAY implied price using ETSY | $229.36 |
| Mechanical peer-implied band | $202.65–$229.36 |

This is a conditional arithmetic band, not a confidence interval or a defended fair-value range. Both peers are qualified, and two observations do not establish a representative market multiple. The target price is below the band, but that alone does not establish mispricing.

## Arithmetic and peer-removal validation

Worked arithmetic to reproduce by hand:

ETSY P/E = 73.46 / 1.39 = 52.8489208633…

EBAY implied price = (73.46 / 1.39) × 4.34 = 229.3643165468… = $229.36.

The calculator uses unrounded ratios. An independent high-precision decimal check gives the midpoint price as 216.0062877150…, displayed as $216.01.

**Prediction to understand before rerunning:** Etsy is the higher-multiple peer. Removing it should lower the median-implied estimate; removing MercadoLibre should raise it. This explanation is prepared with the results available and is not represented as a separately recorded student prediction.

| Removed peer | Remaining peer | Remaining estimate | Change from unrounded full estimate |
|---|---|---:|---:|
| ETSY | MELI | $202.65 | −$13.36 |
| MELI | ETSY | $229.36 | +$13.36 |

The direction matches the reasoning. With one remaining peer there is a reference estimate, not a range; removing that sole peer leaves no estimate. Neither removal is a decision to discard a business merely because of its valuation result.

Software checks passed for the original Asbury midpoint and removal result, independent decimal arithmetic, duplicate symbols, target exclusion, policy exclusions, missing/nonpositive/nonfinite inputs, one peer, and no peers. See `lab08_results.txt` for the actual company run.

## DCF comparison — missing work is explicit

| Method | Company result and date | Main assumption or limitation |
|---|---|---|
| Week 3 company DCF | No completed EBAY range available | Missed company exercise; incomplete cash/investment adjustment and acquisition forecast. |
| Validated training DCF | $27.4974 point value; $21.06–$39.02 sensitivity range; no company valuation date | Hypothetical inputs. NOT an eBay result and not numerically comparable. |
| Peer P/E | EBAY, September 16, 2026: mechanical $202.65–$229.36 band; midpoint $216.01 | Qualified peers and FY2025 earnings; business-perimeter and earnings-quality limitations. |

The drafted DCF research calculates historical starting FCFF of $1,686.24 million using the lab formula and an assumed 21% interest tax shield. Its forecast rates (5%, 4%, 4%, 3%, 3%), approximately 9.28% WACC and 2.5% terminal growth are preliminary assumptions, not a completed valuation.

The [Q2 filing](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000177/ebay-20260630.htm), balance sheet and Note 9, reports June cash of $2,310 million and debt of $6,735 million. Its acquisition discussion reports $1.4 billion cash paid for Depop on July 30. June cash less that payment is not a verified September cash balance. Acquired cash, other movements, investment treatment, operating cash needs, and Depop's cash-flow contribution need consistent treatment. The simple FCFF formula also warrants checking for non-operating investment income before separately adding investments.

Accordingly, no combined valuation range or numerical DCF-versus-P/E conclusion is presented. This documents the gap but does **not** claim to satisfy the requested saved Week 3 company DCF comparison. eBay's P/E itself is usable; missing DCF work is not a nonpositive-EPS exception.

## Skeptical AI review and proposed judgments

Provisional call before criticism: watch-defer. The mechanical band is insufficient evidence to initiate.

| AI criticism | Proposed judgment | Evidence/reason |
|---|---|---|
| The weakest assumption is that the peers' consolidated earnings deserve transferable multiples. | Accept | The cited business sections show different economics; Etsy's Note 6 identifies an impairment that depresses the denominator. |
| Date alignment of prices is not enough: FY2025 business scope differs from September scope. | Accept | Annual earnings and the Depop closing disclosure establish the timing mismatch. |
| A combined range cannot be supported without the missing EBAY DCF. | Accept | Only a hypothetical training result has been validated. |
| The current multiple gap proves eBay is undervalued. | Reject | This claim does not follow from qualified peers and historical EPS. |
| The precise effect of Depop and recurring earnings on the valuation is known. | Unresolved | The present work does not establish a comparable normalized annual earnings base or full combined cash-flow forecast. |

These judgments are proposed by the assistant for my review, not evidence that I independently evaluated the advice. No second independent AI consultation is claimed.

**Question that could change the decision:** Would the apparent discount survive a consistent treatment of recurring earnings and business scope, and would a completed eBay DCF support an upside after allowing for uncertainty?

**Draft answer:** That has not been demonstrated. It is the evidence needed before treating the multiple gap as an opportunity. The earnings definition in this lab remains total reported diluted EPS; I would not silently replace it with an adjusted figure to obtain a desired answer.

## Conditional conclusion and explanation

**Watch-defer.** I can defend the calculations given their inputs, but I withhold a fair-value range. The peer method adds market evidence about how other businesses' earnings are priced; it does not independently validate my forecast. With no completed company DCF, I cannot explain a numerical disagreement between the two methods or average them.

I would reconsider initiation only after completing the cash-flow model and source checks, if the market price were at least 20% below the lower end of a newly defensible valuation range and the peer evidence remained supportive. The 20% threshold is a chosen decision rule, not a proven margin of safety and not a threshold applied to the current mechanical band.

Monitor the next reported operating cash flow, operating margin, and Depop integration disclosures. Updated evidence about sustainable earnings or the cash needed to run the combined business could change the decision more than a small rounding difference in P/E.

## Run and submit

Put `lab08_comps.py`, this file, and optionally `lab08_results.txt` in the existing course/DCF repository. Preserve Lab 7 and the original training DCF.

From the course folder's PowerShell terminal:

```powershell
& .\.venv\Scripts\python.exe .\lab08_comps.py
```

Student actions still pending: open the cited sources, check the hand calculation, review/adopt or revise the proposed judgments and conclusion, complete any required partner/independent-policy activities, and upload/commit the files and submit their GitHub links. The incomplete Week 3 company DCF remains a substantive assignment gap; it has not been concealed with a training value.

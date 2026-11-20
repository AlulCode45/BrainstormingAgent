#!/usr/bin/env python3
"""Scenario financial model. Usage: model.py inputs.json"""
import json
import sys


def run(i, m, months=12, price=None):
    price = price if price is not None else i["price"]
    units = i["month1_units"] * m["units"]
    growth = i["monthly_growth"] * m["growth"]
    vc = i["unit_variable_cost"] * m["cost"]
    fixed = i["monthly_fixed_costs"] * m["cost"]
    cash, rows, breakeven = i["starting_cash"], [], None
    for mo in range(1, months + 1):
        profit = units * (price - vc) - fixed - units * i["cac"]
        cash += profit
        if breakeven is None and profit >= 0:
            breakeven = mo
        rows.append((mo, round(units), round(units * price), round(profit), round(cash)))
        units *= 1 + growth
    burn = [-r[3] for r in rows if r[3] < 0]
    runway = ">12" if cash > 0 and burn else ("n/a" if not burn else "<12")
    ltv = (price - vc) * i["repeat_orders_per_customer"]
    return rows, breakeven, runway, ltv, min(r[4] for r in rows)


def main():
    i = json.load(open(sys.argv[1]))
    c = i.get("currency", "")
    print(f"# Model Output ({c})\n")
    for name, m in i["scenario_multipliers"].items():
        rows, be, runway, ltv, low = run(i, m)
        print(f"## Scenario: {name}\n")
        print("| Month | Units | Revenue | Profit | Cash |\n|---|---|---|---|---|")
        for r in rows:
            print("| " + " | ".join(f"{x:,}" for x in r) + " |")
        print(f"\n- Break-even month: {be or 'not within 12 months'}")
        print(f"- Lowest cash point: {low:,}  ({'CASH SHORTFALL' if low < 0 else 'ok'})")
        print(f"- Runway: {runway}")
        print(f"- LTV: {ltv:,.0f} | CAC: {i['cac']:,} | LTV/CAC: {ltv / i['cac']:.1f}\n")
    base = i["scenario_multipliers"]["base"]
    print("## Sensitivity (base scenario, month-12 cash)\n")
    print("| Price change | Month-12 cash |\n|---|---|")
    for d in (-0.2, -0.1, 0, 0.1, 0.2):
        rows, *_ = run(i, base, price=i["price"] * (1 + d))
        print(f"| {d:+.0%} | {rows[-1][4]:,} |")


if __name__ == "__main__":
    main()

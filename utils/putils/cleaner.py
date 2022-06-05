
def get_state_pop_totals_from_ready_totals(df):
    _totals = df.copy()
    _totals["dead_100k"] = round(_totals.dead / _totals.population * 100000, 2)
    _totals["injured_100k"] = round(_totals.injured / _totals.population * 100000, 2)
    _totals["total_100k"] = round(_totals.total / _totals.population * 100000, 2)
    return _totals


def get_state_pop_totals_from_summary(df, state_population_df):
    _totals = df.join(state_population_df.set_index("state"), on="state")
    return get_state_pop_totals_from_ready_totals(_totals)


def get_state_pop_totals_from_raw(df, state_population_df):
    _df = df.groupby("state").sum().reset_index()
    return get_state_pop_totals_from_summary(_df, state_population_df)
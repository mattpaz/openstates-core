from ..models import State, Chamber, District

AL = State(
    name="Alabama",
    abbr="AL",
    capital="Montgomery",
    capital_tz="America/Chicago",
    fips="01",
    unicameral=False,
    legislature_name="Alabama Legislature",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        num_seats=105,
        title="Representative",
        districts=None,
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        num_seats=35,
        title="Senator",
        districts=None,
    ),
)

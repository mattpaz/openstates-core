from ..models import State, Chamber, District

UT = State(
    name="Utah",
    abbr="UT",
    capital="Salt Lake City",
    capital_tz="America/Denver",
    fips="49",
    unicameral=False,
    legislature_name="Utah State Legislature",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        num_seats=75,
        title="Representative",
        districts=None,
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        num_seats=29,
        title="Senator",
        districts=None,
    ),
)

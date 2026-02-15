import datetime as dt
from dateutil.relativedelta import relativedelta


def get_target_yyyymm(months_ago: int = 2) -> str:
    """
    Return the year-month string (yyyy-MM) for the given number of months ago.
    """
    target_date = dt.date.today() - relativedelta(months=months_ago)
    return target_date.strftime("%Y-%m")


def get_month_start_n_months_ago(months_ago: int = 2) -> dt.date:
    """
    Return the date representing the 1st day of the month, 'n' months ago.
    """
    first_day_in_curr_month = dt.date.today().replace(day=1)
    return first_day_in_curr_month - relativedelta(months=months_ago)

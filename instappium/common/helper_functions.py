# libraries import
import signal
from contextlib import contextmanager


@contextmanager
def interruption_handler(
    threaded=False,
    SIG_type=signal.SIGINT,
    handler=signal.SIG_IGN,
    notify=None,
    logger=None,
):
    """ Handles external interrupt, usually initiated by the user like
    KeyboardInterrupt with CTRL+C """
    if notify is not None and logger is not None:
        logger.warning(notify)

    if not threaded:
        original_handler = signal.signal(SIG_type, handler)

    try:
        yield

    finally:
        if not threaded:
            signal.signal(SIG_type, original_handler)


def truncate_float(number, precision, do_round=False):
    """ Truncate (shorten) a floating point value at given precision """

    # don't allow a negative precision [by mistake?]
    precision = abs(precision)

    if do_round:
        # python 2.7+ supported method [recommended]
        short_float = round(number, precision)

        # python 2.6+ supported method
        """short_float = float("{0:.{1}f}".format(number, precision))
        """

    else:
        operate_on = 1  # returns the absolute number (e.g. 11.0 from 11.456)

        for _ in range(precision):
            operate_on *= 10

        short_float = float(int(number * operate_on)) / operate_on

    return short_float

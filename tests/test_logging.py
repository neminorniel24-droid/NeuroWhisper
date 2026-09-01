import logging

from eeg_isr.utils.logging import get_logger


def test_get_logger():
    logger = get_logger("eeg_isr.test")

    assert isinstance(logger, logging.Logger)
    assert logger.level == logging.INFO

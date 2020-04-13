import logging

import os

from pathlib import Path

from apps.misc.logging_utils import setup_logging
from apps.misc.open_file import read_file, obtain_stream


def generate_common_term(a_word: str) -> str:
    """
    Convert the provided term to a lower case function
    :param a_word:
    :return:
    """
    return a_word.lower().replace(' ', '')


def no_strategy(a_word: str) -> str:
    """
    For the sake of brevity and pep8...
    :param a_word:
    :return: str
    """
    return a_word


def find_term_with_generator(will_not_merge_terms: bool, storage: dict) -> None:
    """
    We will receive a term that we will use to lookup via a generator.

    :param will_not_merge_terms: bool If this is true we will use
    a custom strategy that will change how we index data in the storage.
    :param storage: dict Our internal "storage"
    :return: None
    """

    internal_storage = storage
    strategy_index = generate_common_term

    if will_not_merge_terms:
        strategy_index = no_strategy

    while True:
        term = yield
        indexed_term = strategy_index(term)

        if indexed_term not in internal_storage:
            internal_storage.update({indexed_term: [term]})
        else:
            internal_storage[indexed_term].append(term)


def app(will_not_merge_terms: bool):
    """
    Open a file with cameras and read the content
    :param will_not_merge_terms: bool Merge or not the index of our storage
    :return:
    """
    storage = {}
    filename = Path(__file__, "../assets/camera_list.txt")
    setup_logging(Path(__file__, "../../logging.json").resolve())
    logger = logging.getLogger(__file__)

    logger.debug("Running")
    finder = find_term_with_generator(will_not_merge_terms, storage)
    finder.send(None)
    try:
        logger.debug("Opening file.")
        with obtain_stream(filename.resolve()) as file_handler:
            for word in read_file(file_handler):
                finder.send(word)

        for term, matches in sorted(storage.items()):
            logger.info(f"{term.strip()}: {len(matches)}")
        logger.debug(f"You run with SHOULD_INDEX: {os.getenv('SHOULD_INDEX')}")
    except IOError:
        logging.exception("Could not open the file")


if __name__ == '__main__':

    will_index = os.getenv("SHOULD_NOT_INDEX", False)
    app(will_index)

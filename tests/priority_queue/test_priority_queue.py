import pytest
from ting_file_management.priority_queue import PriorityQueue

mock_one_line = {
    "nome_do_arquivo": "text-one-line.txt",
    "qtd_linhas": 1,
    "linhas_do_arquivo": ["This is the first text's line"],
}

mock_three_line = {
    "nome_do_arquivo": "text-three-line.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [
        "This is the first text's line",
        "This is the second text's line",
        "This is the thirt text's line",
    ]
}

mock_six_line = {
    "nome_do_arquivo": "text-six-line.txt",
    "qtd_linhas": 6,
    "linhas_do_arquivo": [
        "This is the first text's line",
        "This is the second text's line",
        "This is the thirt text's line",
        "This is the fourth text's line",
        "This is the fifth text's line",
        "This is the sixth text's line",
    ]
}


def test_basic_priority_queueing():
    first_queue_test = PriorityQueue()
    first_queue_test.enqueue(mock_one_line)
    first_queue_test.enqueue(mock_six_line)
    first_queue_test.enqueue(mock_three_line)

    assert len(first_queue_test) == 3

    third_position = first_queue_test.search(2)
    first_position = first_queue_test.search(0)

    assert third_position["nome_do_arquivo"] == 'text-six-line.txt'
    assert first_position["nome_do_arquivo"] == 'text-one-line.txt'

    first_queue_test.dequeue()

    new_first_position = first_queue_test.search(0)["nome_do_arquivo"]
    assert new_first_position == 'text-three-line.txt'

    second_queue_test = PriorityQueue()

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        second_queue_test.search(1)

from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():

    priority_queue_list = [
        {"nome_do_Arquivo": 'test1', "qtd_linhas": 2, 'linhas_do_arquivo': []},
        {"nome_do_Arquivo": 'test2', "qtd_linhas": 9, 'linhas_do_arquivo': []},
    ]

    priority_queue = PriorityQueue()

    assert priority_queue.is_priority(priority_queue_list[0]) is True
    assert priority_queue.is_priority(priority_queue_list[1]) is False

    priority_queue.enqueue(priority_queue_list[0])
    priority_queue.enqueue(priority_queue_list[1])

    assert len(priority_queue.high_priority) == 1
    assert len(priority_queue.regular_priority) == 1
    assert len(priority_queue) == 2

    assert priority_queue.search(0) == priority_queue_list[0]

    assert priority_queue.dequeue() == priority_queue_list[0]

    with pytest.raises(IndexError):
        priority_queue.search(1)

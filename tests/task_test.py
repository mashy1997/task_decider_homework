import unittest
from src.task import Task
from src.task_decider import *

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task1 = Task("wash dishes", 60)
        self.task2 = Task("cook dinner", 30)
        self.task3 = Task("clean window", 20)

    
    def test_dishes_over_dinner(self):
        selected_option = get_preffered_option(self.task1, self.task2)
        self.assertEqual(self.task1, selected_option)

    def test_window_over_dishes(self):
        selected_option1 = get_preffered_option(self.task1, self.task3)
        self.assertEqual(self.task3, selected_option1)

    def test_dinner_over_window(self):
        selected_option2 = get_preffered_option(self.task2, self.task3)
        self.assertEqual(self.task2, selected_option2)
        


import unittest

from app import Todo


class TestTodo(unittest.TestCase):
	def setUp(self):
		self.todo = Todo(content="test")

	def test_init_values(self):
		self.assertEqual(self.todo.content, "test")

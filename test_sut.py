import unittest
from mockito import mock, unstub, verify, when
from unittest_data_provider import data_provider
from sut import Dependency, Sut


test_data = lambda: (
    ('a',),
    ('b',)
)

class TestSut(unittest.TestCase):

    def setUp(self):
        self.dep = mock(Dependency)

    @data_provider(test_data)
    def test_execute(self, value):
        when(self.dep).execute()

        sut = Sut(self.dep)

        sut.execute()

        # This fails on executing the second tuple from test_data
        verify(self.dep, times=1).execute()

    def tearDown(self):
        unstub()

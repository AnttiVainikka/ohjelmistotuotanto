import unittest

from player import Player
from statistics import Statistics

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_search_function(self):
        self.assertEqual(self.statistics.search("Semenko").name,"Semenko")
        self.assertEqual(self.statistics.search("AAA"),None)
    
    def test_team_function(self):
        self.assertEqual(self.statistics.team("PIT")[0].name,"Lemieux")
        self.assertEqual(self.statistics.search("AAA"),None)
    
    def test_top_scorers_function(self):
        self.assertEqual(self.statistics.top_scorers(1)[0].name,"Gretzky")

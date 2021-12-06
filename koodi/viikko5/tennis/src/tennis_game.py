class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def score_board(self):
        scores = {}
        scores[0] = "Love"
        scores[1] = "Fifteen"
        scores[2] = "Thirty"
        scores[3] = "Forty"
        return scores

    def get_score(self):
        scores = self.score_board()
        if self.m_score1 == self.m_score2:
            if self.m_score1 != 4:
                return scores[self.m_score1] + "-All"
            else:
                return "Deuce"
        if self.m_score1 < 4 and self.m_score2 < 4:
            return scores[self.m_score1] + "-" + scores[self.m_score2]

        minus_result = self.m_score1 - self. m_score2
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

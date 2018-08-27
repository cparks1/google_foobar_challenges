from unittest import TestCase
import level_1
import level_2
import level_3


class TestAnswers(TestCase):
    def test_level1_answer(self):
        """
        Level 1 Test cases
        ==========
        Inputs:
            (string) s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
        Output:
            (string) "did you see last night's episode?"

        Inputs:
            (string) s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
        Output:
            (string) "Yeah! I can't believe Lance lost his job at the colony!!
        """
        test_cases = [("wrw blf hvv ozhg mrtsg'h vkrhlwv?",
                       "did you see last night's episode?"),

                      ("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!",
                       "Yeah! I can't believe Lance lost his job at the colony!!")]
        for test_input, test_output in test_cases:
            self.assertEqual(test_output, level_1.answer(test_input))

    def test_level2_answer1(self):
        """
        Level 2 Test cases
        ==========
        Inputs:
            (int) x = 3
            (int) y = 2
        Output:
            (string) "9"

        Inputs:
            (int) x = 5
            (int) y = 10
        Output:
            (string) "96"
        """
        test_cases = [(1, 1, "1"),
                      (1, 2, "2"),
                      (3, 2, "9"),
                      (5, 10, "96"),
                      (3, 3, "13")]
        for x, y, expected_ans in test_cases:
            given_ans = level_2.bunny_prisoner_answer(x,y)
            self.assertEqual(expected_ans, given_ans, "(%d,%d) - Got: %s, Expected: %s" %
                             (x, y, given_ans, expected_ans))

    def test_level2_elevator_maintenance(self):
        """
        Level 2 Test Cases
        ==========
        Inputs:
            (string list) l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
        Output:
            (string list) ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]

        Inputs:
            (string list) l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
        Output:
            (string list) ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]
        """
        test_cases = [(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]),
                      (["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"], ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"])]

        for input_list, expected_output in test_cases:
            self.assertListEqual(expected_output, level_2.elevator_maintenance(input_list))

    def test_level3_lucky_triples(self):
        """
        Test cases
        ==========
        Inputs:
            (int list) l = [1, 1, 1]
        Output:
            (int) 1

        Inputs:
            (int list) l = [1, 2, 3, 4, 5, 6]
        Output:
            (int) 3
        """
        test_cases = [([1, 1, 1], 1),
                      ([1, 2, 3, 4, 5, 6], 3),
                      ([x for x in range(1, 10)], 7)]

        for input_list, expected_output in test_cases:
            #level_3.lucky_triples(input_list)
            self.assertEqual(expected_output, level_3.lucky_triples(input_list))

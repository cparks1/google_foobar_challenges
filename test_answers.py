from unittest import TestCase
import level_1


class TestAnswers(TestCase):
    def test_level1_answer(self):
        test_cases = [("wrw blf hvv ozhg mrtsg'h vkrhlwv?",
                       "did you see last night's episode?"),

                      ("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!",
                       "Yeah! I can't believe Lance lost his job at the colony!!")]
        for test_input, test_output in test_cases:
            self.assertEqual(test_output, level_1.answer(test_input))

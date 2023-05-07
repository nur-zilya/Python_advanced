import unittest

from CI_basics.previous_hw.financial_report import app


class TestAdding(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.base_url = '/add/'

    def test_can_add_correctly(self):
        date = '20230507'
        numb = 7
        response = self.app.get(f"{self.base_url}{date}/{numb}")
        expected_response = 'Today 2023.05.07 expenses are 7'
        self.assertEqual(response.data.decode('utf-8'), expected_response)

    # def test_can_add_with_leading_zeros(self):
    #     date = '202300507'
    #     numb = 7
    #     response = self.app.get(f"{self.base_url}{date}/{numb}")
    #     expected_response = 'Today 2023.05.07 expenses are 7'
    #     self.assertEqual(response.data.decode('utf-8'), expected_response)

    def test_can_calculate_by_year(self):
        year = 2023
        response = self.app.get(f"/calculate/{year}")
        expected_response = 'Year 2023 expenses are 14'
        self.assertEqual(response.data.decode('utf-8'), expected_response)

    def test_can_calculate_by_month(self):
        year = 2023
        month = 5
        response = self.app.get(f"/calculate/{year}/{month}")
        expected_response = 'Monthly expenses are 14'
        self.assertEqual(response.data.decode('utf-8'), expected_response)

    def test_can_handle_no_expenses(self):
        year = 2024
        response = self.app.get(f"/calculate/{year}")
        expected_response = 'No expenses found for the year 2024'
        self.assertEqual(response.data.decode('utf-8'), expected_response)

    def test_add_fails_for_invalid_date(self):
        date = '20230507invalid'
        numb = 7
        response = self.app.get(f"{self.base_url}{date}/{numb}")
        self.assertEqual(response.status_code, 404)


if __name__ ==



if __name__ == "__main__":
    unittest.main()

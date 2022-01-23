import unittest

from logic import check_posted_data


class TestSnippet(unittest.TestCase):

    def test_check_posted_data_first_set(self):
        # testing the check_posted_data method with different input sets

        print(f"Testing function - {check_posted_data.__name__} Set 1")

        data_list = [[{"x": 184, "y": 323}, "add", 200], [{"x": 143, "y": 0}, "division", 302], [{"x": 142}, "division",
                                                                                                 301]]

        for data in data_list:
            result = check_posted_data(data[0], data[1])

            self.assertEqual(result, data[2])

            print(f"Test data - {data}")

    def test_check_posted_data_second_set(self):
        print(f"Testing function - {check_posted_data.__name__} Set 2")
        data_list = [[{"x": 184, "y": 323}, "add", 200], [{"x": 143, "y": 0}, "division", 302], [{"y": 143}, "division",
                                                                                                 301]]

        for data in data_list:
            result = check_posted_data(data[0], data[1])

            self.assertEqual(result, data[2])

            print(f"Test data - {data}")


if __name__ == "__main__":
    import xmlrunner

    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_reports'))

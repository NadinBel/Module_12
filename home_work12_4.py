import unittest
import rt_with_exceptions
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')

    def test_walk(self):
        try:
            horse = rt_with_exceptions.Runner('Вася', -2)
            logging.info('"test_walk" выполнен успешно')
            for x in range(10):
                horse.walk()
            self.assertEqual(horse.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            greyhound = rt_with_exceptions.Runner(2)
            logging.info('"test_run" выполнен успешно')
            for x in range(10):
                greyhound.run()
            self.assertEqual(greyhound.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        pig = rt_with_exceptions.Runner('Rose')
        for x in range(10):
            pig.walk()
        geopard = rt_with_exceptions.Runner('Murzik')
        for x in range(10):
            geopard.run()
        self.assertNotEqual(pig.distance, geopard.distance)


if __name__ == '__main__':
    unittest.main()

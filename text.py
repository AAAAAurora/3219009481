import unittest
from main import main_test

class MyTest(unittest.TestCase):
    def error_path(self):
        main_test('.//text//orig.txt', './/orig.txt', './/text//result.txt')
        raise FileNotFoundError("Sorry, the text does not exist.")

# 文件输入错误的单元测试
    def test1(self):
        with self.assertRaises(FileNotFoundError):
            self.error_path()

# 测试空白文档
    def void_file(self):
        main_test('.//text//orig.txt', './/text/void.txt', './/text//result.txt')
        raise ZeroDivisionError("Sorry, the text is blank.")

    def test2(self):
        with self.assertRaises(ZeroDivisionError):
            self.void_file()

# 对orig.txt与orig_0.8_add.txt进行查重
    def test3(self):
        main_test('.//text//orig.txt', './/text//orig_0.8_add.txt', './/text//result.txt')

# 对orig.txt与orig_0.8_del.txt进行查重
    def test4(self):
        main_test('.//text//orig.txt', './/text//orig_0.8_del.txt', './/text///result.txt')

# 对orig.txt与orig_0.8_dis_1.txt进行查重
    def test5(self):
        main_test('.//text//orig.txt', './/text//orig_0.8_dis_1.txt', './/text//result.txt')

# 对orig.txt与orig_0.8_dis_10.txt进行查重
    def test6(self):
        main_test('.//text//orig.txt', './/text//orig_0.8_dis_10.txt', './/text//result.txt')

# 对orig.txt与orig_0.8_dis_15.txt进行查重
    def test7(self):
        main_test('.//text//orig.txt', './/text//orig_0.8_dis_15.txt', './/text//result.txt')

# 对orig_0.8_add.txt与orig_0.8_del.txt进行查重
    def test8(self):
        main_test('.//text/orig_0.8_add.txt', './/text/orig_0.8_del.txt', './/text//result.txt')

# 对orig_0.8_dis_1.txt与orig_0.8_dis_10.txt进行查重
    def test9(self):
        main_test('.//text//orig_0.8_dis_1.txt', './/text//orig_0.8_dis_10.txt', './/text//result.txt')

# 对orig.txt与orig.txt进行查重
    def test10(self):
        main_test('.//text//orig.txt', './/text/orig.txt', './/text//result.txt')

if __name__ == '__main__':
    unittest.main()
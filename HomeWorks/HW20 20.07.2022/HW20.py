
class MyClass:
    def __init__(self, text: str):
        self.text = text

    def is_palindrome(self):
        for i in range(len(self.text) // 2):
            if self.text[i] != self.text[-1 - i]:
                print("Not palindrome")
                break
        else:
            print("Palindrome")


if __name__ == '__main__':
    example = MyClass("Hello")
    example.is_palindrome()

    example1 = MyClass("голод долог")
    example1.is_palindrome()

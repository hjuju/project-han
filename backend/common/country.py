class Country(object):  # superclass

    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드 입니다.')


class Korea(Country):  # subclass

    def show_name(self):
        print(f'국가 이름은: {self.name}')


def execute():  # 함수형 프로그래밍, 선언
    k = Korea()
    k.name = '대한민국'
    k.show_name()


execute()

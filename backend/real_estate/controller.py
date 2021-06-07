from real_estate.housing import Housing
from real_estate.dataset import Dataset


class Controller(object):

    @staticmethod
    def main():

        while 1:
            menu = input(f'0. Exit, 1. 모델생성 2. DF 생성')
            if menu == '0':
                break
            elif menu == '1':
                housing = Housing()
                dataset = Dataset()
                dataset.housing = housing.new_model('housing.xlsx')
                Controller.print_this(dataset.housing)
            elif menu == '2':
                pass
            else:
                pass

    @staticmethod
    def print_this(this):
        n = 10
        print(f'1. Housing 의 Type 은 {type(this)}')
        print(f'2. Housing 의 column 은 {this.columns}')
        print(f'3. Housing 의 상위 {n}개 행은 \n{this.head(n)}')
        print(f'4. Housing null 의 개수 \n{this.isnull().sum()}개')


Controller.main()

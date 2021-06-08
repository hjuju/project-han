from real_estate.services import HousingServices
from real_estate.models import HousingDTO


class HousingApi(object):

    @staticmethod
    def print_this(this):
        n = 10
        print(f'1. Housing 의 Type 은 {type(this)}')
        print(f'2. Housing 의 column 은 {this.columns}')
        print(f'3. Housing 의 상위 {n}개 행은 \n{this.head(n)}')
        print(f'4. Housing null 의 개수 \n{this.isnull().sum()}개')

    @staticmethod
    def main():
        util = HousingServices()
        dto = HousingDTO()
        while 1:
            menu = input(f'0. Exit, 1. 모델생성 2. DF 생성')
            if menu == '0':
                break
            elif menu == '1':
                dto.dframe = util.new_model('housing.xlsx')
                HousingApi.print_this(dto.dframe)
            elif menu == '2':
                pass
            else:
                pass



HousingApi.main()

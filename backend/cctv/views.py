from cctv.models import CctvDTO
from cctv.service import CctvService


class CctvViews(object):

    @staticmethod
    def main():

        service = CctvService()
        data = CctvDTO()

        while 1:
            menu = input(f'0. Exit, 1. 모델생성 2. DF 생성')
            if menu == '0':
                break
            elif menu == '1':
                data.dframe = service.new_models('cctv_in_seoul.csv')
                service.print_dframe(data.dframe)
                data.dframe = service.new_models('crime_in_seoul.csv')
                service.print_dframe(data.dframe)
                data.dframe = service.new_models('police_position.csv')
                service.print_dframe(data.dframe)
                data.dframe = service.new_models('us_unemployment.csv')
                service.print_dframe(data.dframe)
                data.dframe = service.new_models_excel('pop_in_seoul.xls')
                service.print_dframe(data.dframe)
            elif menu == '2':
                pass
            else:
                pass


CctvViews.main()

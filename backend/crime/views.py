from crime.service import CrimeService
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


class CrimeAPI(object):

    @staticmethod
    def main():
        crimeservice = CrimeService()
        while 1:
            menu = input('0-Exit\n1-서울CCTV DF\n2-서울범죄 DF\n'
                         '3-경찰서위치 DF\n4-실업율 DF\n5-엑셀POP'
                         '\n6-geo_simple.json\n7us-states\n번호입력: ')
            if menu == '0':
                break
            elif menu == '1':
                crimeservice.csv({'context': './data/', 'fname': 'cctv_in_seoul'})
            elif menu == '2':
                crimeservice.csv({'context': './data/', 'fname': 'crime_in_seoul'})
            elif menu == '3':
                crimeservice.csv({'context': './data/', 'fname': 'police_position'})
            elif menu == '4':
                crimeservice.csv({'context': './data/', 'fname': 'us_unemployment'})
            elif menu == '5':
                crimeservice.xls({'context': './data/', 'fname': 'pop_in_seoul'})
            elif menu == '6':
                crimeservice.json({'context': './data/', 'fname': 'geo_simple'})
            elif menu == '7':
                crimeservice.json({'context': './data/', 'fname': 'us-states'})
            else:
                continue


CrimeAPI.main()

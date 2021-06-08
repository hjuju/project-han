from real_estate.models import HousingDTO
import pandas as pd
import xlwings as xw


class HousingServices(object):

    dto = HousingDTO()

    def new_model(self, payload) -> object:
        this = self.dto
        this.context = './data/'
        this.fname = payload

        return pd.read_excel(this.context + this.fname, sheet_name='평균전세')

        '''
        sheet = xw.Book(this.context + payload).sheets['평균전세']  # 암호화 된 엑셀 푸는 방법
        row_num = sheet.range(1, 1).end('down').end('down').end('down').row
        data_range = 'A2:GE' + str(row_num)
        df = sheet[data_range].options(pd.DataFrame, index=False, header=True).value
        return df
        '''

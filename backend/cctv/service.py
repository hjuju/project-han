from cctv.models import CctvDTO
from common.services import CommonServices
import pandas as pd


class CctvService(CommonServices):

    dto = CctvDTO()

    def new_models(self, payload) -> object:
        this = self.dto
        this.context = './data/'
        this.fname = payload

        return pd.read_csv(this.context + this.fname)

    def new_models_excel(self, payload) -> object:
        this = self.dto
        this.context = './data/'
        this.fname = payload

        return pd.read_excel(this.context + this.fname, sheet_name='YainSoft_Excel1')

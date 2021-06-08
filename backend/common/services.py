class CommonServices(object):

    def print_dframe(self, this):

        n = 10
        print('*'*100)
        print(f'1. Target 의 Type 은 {type(this)}')
        print(f'2. Target 의 column 은 {this.columns}')
        print(f'3. Target 의 상위 {n}개 행은 \n{this.head(n)}')
        print(f'4. Target null 의 개수 \n{this.isnull().sum()}개')


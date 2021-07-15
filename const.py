class const:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise Exception('변수에 값을 할당할 수 없습니다.')
        self.__dict__[name] = value
    def __delattr__(self, name, value):
        if name in self.__dict__:
            raise Exception('변수를 삭제할 수 없습니다.')

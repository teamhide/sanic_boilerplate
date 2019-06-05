from copy import deepcopy


class QueryBuilder:
    """
    query()를 통해 체이닝된 쿼리를 한번 사용하면 기존 쿼리 목록은 지워집니다.
    따라서 query() 이후에는 쿼리를 새롭게 작성해야 합니다.
    """
    def query(self):
        result = deepcopy(self.__dict__)
        self.__dict__.clear()
        return result

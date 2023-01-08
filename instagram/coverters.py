class YearConverter:
    regex =r"20\d{2}"

    def to_python(self, value):
        return int(value) #view 함수 호출되기전에 인자를 한번 정리

    def to_url(self, value):
        return str(value) #url 리버스할때 URL 문자열로 변환

class MonthConverter(YearConverter):
    regex = r"\d{1,2}"

class DayConverter(YearConverter):
    regex = r"[0123]\d"
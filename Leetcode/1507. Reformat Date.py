class Solution:
    def reformatDate(self, date: str) -> str:
        res = re.match(r'(\d{1,2})[a-z]{2} ([a-zA-Z]{3}) (\d{4})', date)
        monthdict = dict(zip(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], range(1, 13)))
        year, month, day = res.group(3), monthdict[res.group(2)], res.group(1)
        return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
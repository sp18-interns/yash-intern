import datetime


class Experience:

    def __init__(self,
                 start_date: datetime = datetime.datetime.now(),
                 end_date: datetime = datetime.datetime.now(),
                 company_name: str = "XXX",
                 designation: str = "Full Stack Developer",
                 is_present: bool = False
                 ):
        self.start_date = start_date
        self.end_date = end_date
        self.company_name = company_name
        self.designation = designation
        self.is_present = is_present
        if self.is_present:  # Good question when to use is_present and when to use self.is_present
            self.end_date = None

    def __str__(self):
        if self.is_present:
            end_date = "Present"
        else:
            end_date = self.end_date
        return f"Working in {self.company_name} as {self.designation} from {self.start_date} to {end_date}"
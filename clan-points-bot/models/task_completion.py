from datetime import date


class TaskCompletion:
    def __init__(
        self,
        screenshot_url: str,
        task_name: str,
        date_achieved: date,
        point_amount: int,
    ):
        self.screenshot_url = screenshot_url
        self.task_name = task_name
        self.date_achieved = date_achieved
        self.point_amount = point_amount

    def to_dict(self):
        return {
            "screenshot_url": self.screenshot_url,
            "task_name": self.task_name,
            "date_achieved": self.date_achieved,
            "point_amount": self.point_amount,
        }

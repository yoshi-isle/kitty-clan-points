class Task:
    def __init__(self,
                 data: dict = None,
                 is_active: bool = None,
                 task_name: str = None,
                 task_id: int = None,
                 point_value: int = None,
                 image_url: str = None,
                 approved_by: str = None):
        if data:
            self.is_active=data.get('is_active')
            self.task_name=data.get('task_name')
            self.task_id=data.get('task_id')
            self.point_value=data.get('point_value')
            self.image_url=data.get('image_url')
            self.approved_by=data.get('approved_by')
        else:
            self.is_active=is_active
            self.task_name=task_name
            self.task_id=task_id
            self.point_value=point_value
            self.image_url=image_url
            self.approved_by=approved_by  

    def to_dict(self):
        return {
            "is_active": self.is_active,
            "task_name": self.task_name,
            "task_id": self.task_id,
            "point_value": self.point_value,
            "image_url": self.image_url,
            "approved_by": self.approved_by
        }
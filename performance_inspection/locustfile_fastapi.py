from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def load_test(self):
        self.client.get("/")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Simulate waiting between tasks (1 to 5 seconds)

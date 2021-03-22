class User:
    # Example of constructor
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password


    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title


    def get_user_info(self):
        print(f"User {self.name} currently works as {self.current_job_title} and you can contact them at {self.email}.")
app_user_one = User("nn@nn.com", "Nana Janshia", "pwd1", "DevOps Engineer")

app_user_one.get_user_info()
app_user_one.change_job_title("Devops trainer")
app_user_one.get_user_info()
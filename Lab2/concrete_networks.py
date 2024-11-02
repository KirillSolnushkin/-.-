from social_network import SocialNetwork, SocialNetworkFactory


class Facebook(SocialNetwork):
    def connect(self, login: str, password: str) -> bool:
        print(f"Підключення до Facebook за допомогою логіну: {login}")
        self.is_connected = True
        return True

    def post_message(self, message: str) -> bool:
        if not self.is_connected:
            raise Exception("Не підключений до Facebook")
        print(f"Публікація на Facebook: {message}")
        return True


class LinkedIn(SocialNetwork):
    def connect(self, email: str, password: str) -> bool:
        print(f"Підключення до LinkedIn за допомогою електронної пошти: {email}")
        self.is_connected = True
        return True

    def post_message(self, message: str) -> bool:
        if not self.is_connected:
            raise Exception("Не підключено до LinkedIn")
        print(f"Публікація в LinkedIn: {message}")
        return True


class FacebookFactory(SocialNetworkFactory):
    def create_network(self) -> SocialNetwork:
        return Facebook()


class LinkedInFactory(SocialNetworkFactory):
    def create_network(self) -> SocialNetwork:
        return LinkedIn()
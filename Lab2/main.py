from concrete_networks import FacebookFactory, LinkedInFactory


def publish_message(factory, credentials: dict, message: str):
    network = factory.create_network()
    network.connect(**credentials)
    network.post_message(message)
    network.disconnect()


def main():
    facebook_factory = FacebookFactory()
    linkedin_factory = LinkedInFactory()

    message = "Привіт від нашого видавця соціальних мереж!"

    fb_credentials = {
        "login": "testUser123",
        "password": "testPass123"
    }
    publish_message(facebook_factory, fb_credentials, message)

    li_credentials = {
        "email": "testEmail@example.com",
        "password": "test2Pass123"
    }
    publish_message(linkedin_factory, li_credentials, message)


if __name__ == "__main__":
    main()
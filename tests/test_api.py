from . import BaseSetupTest

class LoginTestCase(BaseSetupTest):

    def do_login_test(self):
        response = self.client.AuthJwt.create(self.login_object.copy())
        
        assert "token" in response


class TokenCardTestCase(BaseSetupTest):

    def create_toke_card_test(self):
        response = self.client.TokenCard.create(self.token_card_object.copy())

        assert

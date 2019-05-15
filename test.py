# -*- coding: utf-8 -*-

import unittest
import random
import netpay_ecommerce

class BaseSetupTest(unittest.TestCase):

    client = netpay_ecommerce
    username = "edwin.rivas@netpay.com.mx"
    password = "adm0n2"
    netpay_ecommerce.BASE_URL = "https://cert.netpay.com.mx"
    

    login_object = {
        'security': {
            "userName": username,
            "password": password
        }
    }

    token_card_object = {
        "username": "edwin.rivas@netpay.com.mx",
        "storeApiKey": "QX!zPs1bq5uqMCUSd_IX=W7_Rpp=Byds",
        "customerCard": {
            "cardNumber": "4000000000000002",
            "expirationMonth": "01",
            "expirationYear":  "24",
            "cvv": "123",
            "cardType": "001",
            "cardHolderName": "John Doe"
        }
        }

    risk_manager_object = {  
  "storeApiKey":"QX!zPs1bq5uqMCUSd_IX=W7_Rpp=Byds",
  "riskManager":{
     "promotion":"000000",
     "requestFraudService":{  
        "merchantReferenceCode":"14500056",
        "deviceFingerprintID":"fea7f7888a184a10ae2820969ef3062a",
        "bill":{  
       "city": "San Péter",
         "country": "México",
         "firstName": "Valentín2.",
         "lastName": "Dmitrovích2.",
         "phoneNumber": "811-965-4348-",
         "email":"review@netpay.com.mx",
         "postalCode": "66240",
         "state": "NUEVO LÉON",
         "street1": "Hidalgo 627._éÉ",
         "street2": "Hidalgo 627._éÉ",
         "ipAddress": "127.0.0.1"
        },
        "ship":{  
           "city":"city ship",
           "country":"MX",
           "firstName":"mailto",
       "lastName":"mailto",
           "phoneNumber":"8110111111",
           "postalCode":"12345",
           "state":"state",
           "street1":"street 1",
           "street2":"street 2",
           "shippingMethod":"flatrate_flatrate"
        },
        "itemList":[{  
              "id":"421",
              "productSKU":"wbk012c-Royal Blue-S",
              "unitPrice":"1.0000",
              "productName":"Elizabeth Knit Top",
              "quantity":1,
              "productCode":"Tops & Blouses"
           }
        ],
        "card":{  
           "cardToken":"VSRr14Fe5CThE50FhUNT6vNAM8gzAuZNXn5vSTPwRzMH+yRdDt3v5a9ct7nuBzAvrftOEvBrl71vJbx67vWjiudz4oenzirIQyClN8+hTRM="
        },
    "purchaseTotals":{  
           "grandTotalAmount":"6",
           "currency":"MXN"
        },
        "merchanDefinedDataList":[
    {
      "id": "2",
      "value": "Web"
    },
    {
      "id": "4",
      "value": "515"
    },
    {
      "id": "5",
      "value": "0"
    },
    {
      "id": "6",
      "value": "0"
    },
    {
      "id": "7",
      "value": "0"
    },
    {
      "id": "9",
      "value": "Retail"
    },
    {
      "id": "10",
      "value": "3D"
    },
    {
      "id": "11",
      "value": "flatrate_flatrate"
    },
    {
      "id": "13",
      "value": "N"
    },
    {
      "id": "14",
      "value": "Domicilio"
    },
    {
      "id": "16",
      "value": "50000"
    },
    {
      "id": "8",
      "value": "7369687"
    },
    {
      "id": "17",
      "value": "7369687"
    },
    {
      "id": "18",
      "value": "1"
    }]
     }
  }
}

    def get_jwt_token(self):
        response = netpay_ecommerce.AuthJwt.create(self.login_object)
        return response["token"]

    


class ApiTestCase(BaseSetupTest):

    def test_do_logint(self):
        response = self.client.AuthJwt.create(self.login_object.copy())

        assert "token" in response

    def test_create_token_card(self):
        self.token_card_object["customerCard"]["cardNumber"] = "400000000000" + str(self._random_4_digits())
        token = self.get_jwt_token()
        response = self.client.TokenCard.create(data = self.token_card_object.copy(),token=token)

        assert "response" in response
        assert response["response"]["customerToken"]["username"] == self.username

    def test_create_risk_manager_trasanction(self):
        token = self.get_jwt_token()
        response = self.client.RiskManager.create(data=self.risk_manager_object,token=token)

        assert "transactionTokenId" in response

    def _random_4_digits(self):
        return random.randint(1000,9999)    

        
if __name__ == '__main__':
    unittest.main()
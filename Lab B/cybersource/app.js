const express = require('express');
const bodyParser = require('body-parser');
const ejs = require('ejs');
const CyberSourceRestClient = require('cybersource-rest-client');

const app = express();
const port = 3000;

// Configure CyberSource credentials
const merchantId = 'your_merchant_id';
const apiKey = 'your_api_key';
const apiSecretKey = 'your_api_secret_key';
const cybsClient = new CyberSourceRestClient();
cybsClient.enableDebug(true);
cybsClient.setMerchantId(merchantId);
cybsClient.setApiKey(apiKey);
cybsClient.setSecretKey(apiSecretKey);

// Configure EJS view engine
app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

// Middleware for parsing form data
app.use(bodyParser.urlencoded({ extended: true }));

// Route for displaying the checkout page
app.get('/', (req, res) => {
  res.render('checkout');
});

// Route for processing the payment
app.post('/processPayment', (req, res) => {
  const request = {
    clientReferenceInformation: {
      code: 'YOUR_ORDER_ID'
    },
    processingInformation: {
      commerceIndicator: 'internet'
    },
    paymentInformation: {
      card: {
        number: req.body.cardNumber,
        expirationMonth: req.body.expirationMonth,
        expirationYear: req.body.expirationYear,
        securityCode: req.body.cvv
      }
    }
  };

  cybsClient.paymentRequest(request, (error, data, response) => {
    if (error) {
      console.error('Error processing payment:', error);
      res.render('result', { success: false, error: error });
    } else {
      console.log('Payment processed successfully:', data);
      res.render('result', { success: true });
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

const crypto = require("crypto");

const express = require("express");
const uuid = require("uuid");
const bodyParser = require("body-parser");
const cors = require("cors");
const { pick } = require("ramda");

const config = require("./config");

const app = express();

// Serve static files from the "resources" directory
app.use(express.static('resources'));

app.set("view engine", "pug");

app.use(bodyParser.urlencoded({ extended: true }));

const UNSIGNED_FIELD_NAMES = [ 
  "card_number"
 ];

const SIGNED_FIELD_NAMES = [
  "access_key",
  "amount",
  "bill_to_address_city",
  "bill_to_address_country",
  "bill_to_address_line1",
  "bill_to_email",
  "bill_to_forename",
  "bill_to_surname",
  "card_expiry_date",
  "card_type",
  "currency",
  "customer_ip_address",
  "device_fingerprint_id",
  "device_fingerprint_raw",
  "locale",
  "payment_method",
  "profile_id",
  "reference_number",
  "signed_date_time",
  "signed_field_names",
  "transaction_type",
  "transaction_uuid",
  "unsigned_field_names",
  "recurring_start_date",
  "recurring_frequency"
];

app.get("/", (req, res) => {
  const locals = {
    accessKey: config.cybersource.ACCESS_KEY,
    customerIpAddress: req.ip,
    deviceFingerprintId: uuid.v4(),
    orgId: config.cybersource.ORG_ID,
    profileId: config.cybersource.PROFILE_ID,
    referenceNumber: uuid.v4(),
    signedFieldNames: SIGNED_FIELD_NAMES.join(","),
    unsignedFieldNames: UNSIGNED_FIELD_NAMES.join(",")
  };

  res.render("checkout", locals);
});
/*
app.post("/", cors({ origin: config.CORS_ALLOWED_HOSTS }), (req, res) => {
  const { body: input } = req;
  const allFieldsToSign = {
    ...pick(SIGNED_FIELD_NAMES, input),
    signed_date_time: convertToSignatureDate(new Date()),
    signed_field_names: SIGNED_FIELD_NAMES.join(","),
    unsigned_field_names: UNSIGNED_FIELD_NAMES.join(",")
  };

  if (input.recurring_start_date && input.recurring_frequency) {
    allFieldsToSign.recurring_start_date = input.recurring_start_date;
    allFieldsToSign.recurring_frequency = input.recurring_frequency;
  }

  const signature = sign(allFieldsToSign);

  res.json({ ...allFieldsToSign, signature });
});
*/

app.post("/", cors({ origin: config.CORS_ALLOWED_HOSTS }), async (req, res) => {
  try {
    const { card_number, ...input } = req.body;
    const allFieldsToSign = {
      ...pick(SIGNED_FIELD_NAMES, input),
      signed_date_time: convertToSignatureDate(new Date()),
      signed_field_names: SIGNED_FIELD_NAMES.join(","),
      unsigned_field_names: UNSIGNED_FIELD_NAMES.join(",")
    };

    if (input.recurring_start_date && input.recurring_frequency) {
      allFieldsToSign.recurring_start_date = input.recurring_start_date;
      allFieldsToSign.recurring_frequency = input.recurring_frequency;
    }

    const signature = sign(allFieldsToSign);
    const subscriptionData = {
      ...allFieldsToSign,
      signature,
      paymentInformation: {
        card: {
          number: card_number,
          expirationMonth: input.card_expiry_month,
          expirationYear: input.card_expiry_year,
          securityCode: input.card_cvn
        }
      }
    };

    // Create subscription using Cybersource API
    const response = await instance.createSubscription(subscriptionData, configuration);
    console.log(response);
    res.json({ ...allFieldsToSign, signature, success: true });
  } catch (error) {
    console.error('Error creating subscription:', error);
    res.json({ success: false, error: error.message });
  }
});


app.post("/processPayment", (req, res) => {
  const { success, error } = req.body;
  if (success){
    res.render('response', {success:true, error:null});
  }else{
    res.render('response', {success:false, error});
  }
//  res.json(req.body);
});
app.listen(3000);

console.log("Listening at http://localhost:3000");

function convertToSignatureDate(d) {
  const [ isoDate ] = d.toISOString().split(".");

  return `${isoDate}Z`;
}

function sign(fields) {
  const hash = crypto.createHmac("sha256", "SECRET_KEY");
  const encodedFields = Object.keys(fields).sort().map(k => `${k}=${fields[ k ]}`).join(",");

  return hash.update(encodedFields).digest("base64");
}


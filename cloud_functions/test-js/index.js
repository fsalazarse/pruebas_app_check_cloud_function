/**
 * Import function triggers from their respective submodules:
 *
 * const {onCall} = require("firebase-functions/v2/https");
 * const {onDocumentWritten} = require("firebase-functions/v2/firestore");
 *
 * See a full list of supported triggers at https://firebase.google.com/docs/functions
 */

const {onRequest} = require("firebase-functions/v2/https");
const logger = require("firebase-functions/logger");

// Agrega el paquete CORS
const cors = require('cors')({origin: true});
// Create and deploy your first functions
// https://firebase.google.com/docs/functions/get-started

exports.test_js = onRequest((request, response) => {
  logger.info("Hello logs!", {structuredData: true});
  cors(request, response, () => {
    response.status(200).json({"message":"Hello from Firebase!"});
  });
});

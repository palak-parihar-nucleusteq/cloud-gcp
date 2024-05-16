const { onRequest } = require("firebase-functions/v2/https");
const { initializeApp } = require("firebase-admin/app");
const { firestore } = require("firebase-admin");

initializeApp();

exports.handleRequest = onRequest(async (req, res) => {
  console.log('[handleRequest] running inside the http method');

  const collectionName = 'users';

  const documentData = {
    query: req.query.text
  };

  try {
    const collectionRef = firestore().collection(collectionName);
    await collectionRef.add(documentData);

    res.json({ result: `Document added to Firestore` });
  } catch (error) {
    console.error('Error adding document: ', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});


exports.exportData = onRequest(async (req, res) => {
  console.log('[handleRequest] running inside the http method');

  const collectionName = 'users';

  try {
    const collectionRef = firestore().collection(collectionName);
    const snapshot = await collectionRef.get();

    // Extract key-value pairs from Firestore documents
    const data = {};
    snapshot.forEach(doc => {
      data[doc.id] = doc.data(); // Assuming doc.id is the key
    });

    res.json({ data });
  } catch (error) {
    console.error('Error listing document: ', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

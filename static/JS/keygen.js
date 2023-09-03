// Function to generate PEM-encoded RSA key pair
async function generateRSAKeyPair() {
    try {
      // Generate an RSA key pair with a modulus length of 2048 bits
      const keyPair = await window.crypto.subtle.generateKey(
        {
          name: 'RSA-OAEP',
          modulusLength: 2048,
          publicExponent: new Uint8Array([0x01, 0x00, 0x01]), // 65537
          hash: { name: 'SHA-256' },
        },
        true, // Can extract private key
        ['encrypt', 'decrypt']
      );
  
      // Export the public key in PEM format
      const publicKeyPEM = await exportPublicKey(keyPair.publicKey);
  
      // Export the private key in PEM format
      const privateKeyPEM = await exportPrivateKey(keyPair.privateKey);
  
      return { publicKeyPEM, privateKeyPEM };
    } catch (error) {
      console.error('Key generation error:', error);
      return null;
    }
  }
  
  // Function to export a public key in PEM format
  async function exportPublicKey(publicKey) {
    const publicKeyDER = await window.crypto.subtle.exportKey('spki', publicKey);
    const publicKeyPEM = convertBinaryToPEM(publicKeyDER, 'PUBLIC KEY');
    return publicKeyPEM;
  }
  
  // Function to export a private key in PEM format
  async function exportPrivateKey(privateKey) {
    const privateKeyDER = await window.crypto.subtle.exportKey('pkcs8', privateKey);
    const privateKeyPEM = convertBinaryToPEM(privateKeyDER, 'PRIVATE KEY');
    return privateKeyPEM;
  }
  
  // Helper function to convert binary data to PEM format
  function convertBinaryToPEM(binaryData, type) {
    const base64 = btoa(String.fromCharCode(...new Uint8Array(binaryData)));
    const pemHeader = `-----BEGIN ${type}-----`;
    const pemFooter = `-----END ${type}-----`;
    const pemBody = base64.match(/.{1,64}/g).join('\n');
    return `${pemHeader}\n${pemBody}\n${pemFooter}`;
  }
  window.client = window.client || {};
  generateRSAKeyPair().then(({ publicKeyPEM, privateKeyPEM }) => {
        window.client.id_rsa = privateKeyPEM
        window.client.id_rsa_pub = btoa(publicKeyPEM)
  });
  
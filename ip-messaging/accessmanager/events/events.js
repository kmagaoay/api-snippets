accessManager.on('tokenExpired', () => {
  // generate new token here and set it to the accessManager
  let updatedToken = generateToken(); 
  accessManager.updateToken(updatedToken);
});

function usersGetAllGet() {
  var response =  getAPI('http://172.22.42.23:8080/users/getAll');
  for(user in response){
    if (!["Anfaenger", "Fortgeschritten", "Profi"].includes(user.laufniveau ))
    {
      user.laufniveau = "Anfaenger";
    }
  }
  return response;
}

function getSearch(searchString) {
  return getAPI('http://192.168.43.202:8080/users/getSearch?searchString=' + encodeURI(searchString) + '&skip=0&limit=10')
}

function login(username, password){
  return getAPI('http://192.168.43.202:8080/login?username=' + encodeURI(username) + '&password=' + encodeURI(password))
}

function getAPI(URL, errorFunc=null) {
  let didTimeOut = false;
  return new Promise(function(resolve, reject) {
      const timeout = setTimeout(function() {
          didTimeOut = true;
          reject(new Error('Request timed out'));
      }, 2500);

      fetch(URL)
      .then(function(response) {
          clearTimeout(timeout);
          if(!didTimeOut) {
              resolve(response);
          }
      })
      .catch(function(err) {
          if(didTimeOut) return;
          // Reject with other error, besides timeout
          reject(err);
          errorFunc();
      });
  })
  .then(function(response) {
      if (response.ok) {
        return response.json();
      } else {
        return Promise.reject(Error('error'));
      }
  }).then(function(data){
    return data;
  })
  .catch(function(err) {
      console.log('error: ', err);
  });
}



function mock() {
  return [{
      name: "Joseph",
      laufort: "45372",
      laufniveau: 3,
      eMail: "hdhd@hh.de"
    },
  {
    name: "Hallo",
    laufort: "98965",
    laufniveau: 1,
    eMail: "hdhd@hh.de"
  }]
}

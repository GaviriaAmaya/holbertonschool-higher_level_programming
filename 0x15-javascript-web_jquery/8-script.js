$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
})
  .done(function (json) {
    for (const results of json.results) {
      $('UL#list_movies').append('<li>' + results.title + '</li>');
    }
  });

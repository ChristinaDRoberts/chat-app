// javascript to make the ajax requests and set interval to 30 seconds
//
//
(function($){
  $(function(){
    console.log('Working!');

    // You need to send a CSRF Token when POSTing
    // You do this by adding this to your project
    // https://docs.djangoproject.com/en/2.1/ref/csrf/#setting-the-token-on-the-ajax-request
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // AJAX Request to get a list of items
    // A string containing the URL to which the request is sent.
    //   in search bar it automatically has localhost:8000 before it
    $.ajax('/api/message/', {
        'dataType': 'json',
        'error': function(resp, err){console.log(resp, err)},
        'success': function (data) {
            // show me the data we are recieving in the console
        console.log('data', data);
        console.log('Way to go Christina, you ARE getting it !')

    // a kind of for loop to return each message
        data.forEach(function(Message){
            // i want these to go into my chat template but they are appending onto bottom
            // of body bc thats what im telling it to do here !
            // this is printing out the messages on browser
          $('body').append('<p>' + Message.text + '</p>');
          // this is printing out the # the user is in browser
          $('body').append('<p>' + Message.user + '</p>');

        })
      }
    });

    // on click event (submit button) post the new message and username to database
    // Register event handler on the .post button
    $('.post').on('click', function(){

      // POST ajax request to actually creat the message
      $.ajax('/api/message/', {
        'method': 'POST',
        'data': {'user': ' user.username', 'message': 'user.message'},

        'success': function(data) {
          console.log('success!');
        }
      });
    });

  });
}(jQuery));




// $(document).ready(function() {
//
//     const BASE_URL = 'http://localhost:/.js';
//
//
//     $.ajax({
//         url: `${'api/message/'}`,
//         dataType: 'jsonp',
//         method: 'GET',
//
//
//         success: function (response) {
//             // console.log('response', response);
//             var source = $("#entry-template").html();
//             var template = Handlebars.compile(source);
//             var context = {
//                 results: response.results
//             }
//             var html = template(context);
//
//             $('.row').html(html);
//         },
//
//
//         error: function (xhr) {
//             console.log('uh oh, something went wrong', xhr.status);
//         }
//
//     })
//
// });
// //

// var chatList = document.getElementByID(‘msg-list-div’);
// chatlist.scrollTop = chatList.scrollHeight;
//
//
// $.get( "ajax/chat.html", function( data ) {
//   $( ".result" ).html( data );
//   alert( "Load was performed." );
// });
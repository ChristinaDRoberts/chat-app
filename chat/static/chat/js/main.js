// javascript to make the ajax requests and set interval to 30 seconds
//
//
// (function($){
//   $(function(){
//     console.log('Working!');
//
//     // You need to send a CSRF Token when POSTing
//     // You do this by adding this to your project
//     // https://docs.djangoproject.com/en/2.1/ref/csrf/#setting-the-token-on-the-ajax-request
//     var csrftoken = $("[name=csrfmiddlewaretoken]").val();
//     function csrfSafeMethod(method) {
//         // these HTTP methods do not require CSRF protection
//         return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//     }
//     $.ajaxSetup({
//         beforeSend: function(xhr, settings) {
//             if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//                 xhr.setRequestHeader("X-CSRFToken", csrftoken);
//             }
//         }
//     });
//
//     // AJAX Request to get a list of items
//     // A string containing the URL to which the request is sent.
//     $.ajax('/api/', {
//       // 'dataType': 'json',
//       'error': function(resp, err){console.log(resp, err)},
//       'success': function (data) {
//         console.log('data', data);
//
//         data.forEach(function(Message){
//           $('body').append('<p>' + Message.text + '</p>');
//           $('body').append('<p>' + Message.user + '</p>');
//
//         })
//       }
//     });
//
//     // Register event handler on the .post button
//     $('.post').on('click', function(){
//
//       // POST ajax request to create a new piece of candy
//       $.ajax('/message/', {
//         'method': 'POST',
//         'data': {'user': ' user.username', 'message': 'user.message'},
//         // 'data': {'name': 'thin mint', 'is_chocolate': true},
//         'success': function(data) {
//           console.log('success!');
//         }
//       });
//     });
//
//   });
// }(jQuery));




$(document).ready(function() {

    const BASE_URL = 'http://localhost:/.js';


    $.ajax({
        url: `${'api/message/'}`,
        dataType: 'jsonp',
        method: 'GET',


        success: function (response) {
            // console.log('response', response);
            var source = $("#entry-template").html();
            var template = Handlebars.compile(source);
            var context = {
                results: response.results
            }
            var html = template(context);

            $('.row').html(html);
        },


        error: function (xhr) {
            console.log('uh oh, something went wrong', xhr.status);
        }

    })

});
//

// var chatList = document.getElementByID(‘msg-list-div’);
// chatlist.scrollTop = chatList.scrollHeight;
//
//
// $.get( "ajax/chat.html", function( data ) {
//   $( ".result" ).html( data );
//   alert( "Load was performed." );
// });
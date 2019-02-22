// javascript to make the ajax requests and set interval to 30 seconds
//
//
(function($) {
    $(function () {
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
            beforeSend: function (xhr, settings) {
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
            'error': function (resp, err) {
                console.log(resp, err)
            },


            'success': function (data) {
                // var source   = document.getElementById(".innerHTML;
                // var template = Handlebars.compile(source);

                // show me the data we are recieving in the console
                console.log('data', data);

                data2 = data.reverse()
                data2.forEach(showMessageItem);
            },

        });


        function showMessageItem(Message) {
            var $li = $('<li></li>');
            $li.append('<p>' + Message.text + '</p>');
            $li.append('<p>' + Message.user.username + '</p>');
            $li.append('<p>' + Message.created + '</p>');
            $li.append('<hr/>');

            $('ul').prepend($li);
        }



        // on click event (submit button) post the new message and username to database
        // Register event handler on the .post button
        $('.add_message_form').on('submit', function (event) {
            var messageUserSent = $('#message_of_user').val();
            event.preventDefault();
            console.log('add message');
            console.log(messageUserSent)

            // POST ajax request to actually create the message
            $.ajax('/api/message/', {
                'method': 'POST',
                'data': {'text': messageUserSent},

                'success': function (data) {
                    $('#message_of_user').val('');

                    console.log('success!');
                    showMessageItem(data);
                },
                'error': function () {
                    console.log("go back and fix it")
                }
            });
        });

    });

}(jQuery));
// semicolons come at end of expressions




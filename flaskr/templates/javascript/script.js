<script>

//this is called when the page loads
$(document).ready(function() {
    $('#boolean1').val({{device.boolean1}}); //set the default values for element <input id=boolean1> in index.html
    $('#boolean2').val({{device.boolean2}}); //more default values
    $('#integer1').val({{device.integer1}}); //more

    //this is called when <button id=submit-btn> element is clicked in index.html
    $('#submit-btn').click(function() {
        var boolean1 = $('#boolean1').val(); //get current value of element <input id=boolean1>
        var boolean2 = $('#boolean2').val(); //get value of element
        var integer1 = $('#integer1').val(); //get value of element

        //sends a POST request to /update where request.form['boolean1'] is = boolean1 in the browser and flashes a message
        $.ajax({
            url: "{{ url_for('index.update') }}",
            type: "POST",
            headers: {'AJAX': 1},
            data: { 'boolean1': boolean1, 'boolean2': boolean2, 'integer1': integer1},
            success: function(json){
                $('#submit-confirmation').flash_message({
                    text: 'Success!',
                    how: 'append'
                });
            },
            error: function(json) {
                $('#submit-confirmation').flash_message({
                    text: 'Error!',
                    how: 'append'
                });
            }
        });
    });

    //do not change, copy pasted from stackoverflow, code to flash success messages in jquery
    (function($) {
    $.fn.flash_message = function(options) {

      options = $.extend({
        text: 'Done',
        time: 1000,
        how: 'before',
        class_name: ''
      }, options);

      return $(this).each(function() {
        if( $(this).parent().find('.flash_message').get(0) )
          return;

        var message = $('<span />', {
          'class': 'flash_message ' + options.class_name,
          text: options.text
        }).hide().fadeIn('fast');

        $(this)[options.how](message);

        message.delay(options.time).fadeOut('normal', function() {
          $(this).remove();
        });

      });
    };
})(jQuery);


});




</script>

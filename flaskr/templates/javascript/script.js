<script>
$(document).ready(function() {
    $('#boolean1').val({{device.boolean1}});
    $('#boolean2').val({{device.boolean2}});
    $('#integer1').val({{device.integer1}});

    $('#submit-btn').click(function() {
        var boolean1 = $('#boolean1').val();
        var boolean2 = $('#boolean2').val();
        var integer1 = $('#integer1').val();
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

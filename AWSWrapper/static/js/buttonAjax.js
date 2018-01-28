function buttonAjax(buttonElem, options, failOnly) {
    if (failOnly === undefined) {
        failOnly = false;
    }

    // Get original html and click events
    var html = buttonElem.html();

    // Disable button
    buttonElem
        .prop('disabled', true)
        .css('pointer-events', 'none')
        .css('cursor', 'not-allowed');

    // Set spinner
    var icons = buttonElem.find('i.fa');
    if (icons.length > 0) {
        // Set icon to spinner
        var icon = $(icons[0]);
        icon.removeClass('fa-*');
        icon.addClass('fa-spinner fa-spin')
    } else {
        // Prepend spinner
        buttonElem.html('<i class="fa fa-spinner fa-spin"></i>&nbsp;' + html);
    }

    var disableFunc = function () {
        // Reset original html
        buttonElem.html(html);

        // Enable button
        buttonElem
            .css('pointer-events', '')
            .prop('disabled', false)
            .css('cursor', '');
    };

    // Send AJAX
    if (failOnly === true) {
        return $.ajax(options).always(fail);
    } else {
        return $.ajax(options).always(disableFunc);
    }
}
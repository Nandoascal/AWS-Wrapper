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

$(document).ready(function () {
    var instance = $('#my-data').data();
    console.log(instance);

    $('#buttonIAMRole').click(function (e) {
        buttonAjax($(this), {
            method: "POST",
            url: "/????",
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonScaling').click(function (e) {
        console.log("buttonscaling")
    });
    $('#buttonType').click(function (e) {
        console.log("buttonType")
    });
    $('#buttonTermination').click(function (e) {
        console.log("buttonTermination")
    });
    $('#buttonUserData').click(function (e) {
        console.log("buttonUserData")
    });
    $('#buttonT2').click(function (e) {
        console.log("buttonT2")
    });
    $('#buttonModifyInstance').click(function (e) {
        console.log("buttonModifyInstance")
    });
    $('#buttonNewInstance').click(function (e) {
        console.log("buttonNewInstance")
    });
    $('#buttonStart').click(function (e) {
        console.log("buttonStart")
    });
    $('#buttonStop').click(function (e) {
        console.log("buttonStop")
    });
    $('#buttonReboot').click(function (e) {
        console.log("buttonReboot")
    });
    $('#buttonKill').click(function (e) {
        console.log("buttonKill")
    });
    $('#dropDownCreateImage').click(function (e) {
        console.log("dropDownCreateImage")
    });
    $('#dropDownBundleInstance').click(function (e) {
        console.log("dropDownBundleInstance")
    });
});

